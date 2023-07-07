"""
用于分拣活动
"""
import asyncio
import re
import time
from urllib import parse

from core import queue
from core.convert import Convert
from db.db_activities import MethodActivities
from db.db_repeats import MethodRepeats
from init.conf import conf
from models.activities import Activities
from models.repeats import Repeats
from schemas.activities import ExportModel
from utils.logs import log


class Points(Convert, MethodActivities, MethodRepeats):
    def __init__(self):
        super().__init__()
        MethodActivities.__init__(self, Activities)
        MethodRepeats.__init__(self, Repeats)
        self.bot = None
        self.chat_id_list: list[int] = conf.tg.forward_from
        self.black_keywords = "|".join(conf.activities.black_keywords)
        self.expired: int = int(time.time()) + 3600
        self.lock = asyncio.Lock()

    async def pie(self, text: str):
        """
        用于把各种值进行分类，缺陷无法判断同一行中同类型
        :param text:
        :type text:
        :return:
        :rtype:
        """
        tg_text = re.sub("[()\;`*\"]*(?:export NOT_TYPE=\".*?\";)*(?:\s转发频道的id\d+)*", "", parse.unquote(text))
        try:
            if self.black_keywords:
                if re.findall(f"(?:{self.black_keywords})+", tg_text):
                    await log.debug("屏蔽关键字存在跳过执行")
                    return
            # 识别正则表达式中是否有关键字信息
            re_identify = re.findall("(?:https://.*?com/|export)+", text)
            if not re_identify:
                return
            tf = False
            for https in re_identify:
                if "https" in https:
                    tf = True
                    break
            if tf:
                # 转换url
                for url in tg_text.split("\n"):
                    # 过滤一些关键字
                    if re.findall(
                            r'((?:s.click.taobao|u.jd|tg://user|suol.cc|618day|github|coupon.m.jd.com|tiny://|nodeseek|t.me)+)',
                            url, re.S):
                        continue
                    # 这里是url部分
                    ht_tx = re.findall(r'(https://[\w\-.]+(?:isv|jd).*?\.com/[a-zA-Z0-9&?=_/-].*)', url)
                    if ht_tx:
                        if not await self.repeat(ht_tx[0]):
                            continue
                        export_va = await self.convert_url(ht_tx)
                        # 下面就是加入队列了
                        if export_va:
                            await self.forward(ht_tx[0])
                            # 准备加入队列任务
                            await log.info(f"加入队列 {export_va}")
                            await queue.put([export_va[0].js_level, export_va])
                            continue
                        else:
                            # 如果没有这里会进入
                            await log.info(f"没有匹配到对应任务 {ht_tx}")
            else:
                tg_list = re.findall("(export [\w_]+)=\"?([\w:/\.\-@&?=]+)\"?", tg_text)
                if not tg_list:
                    return
                select = await self.or_select(tg_list[0][0])
                if not select:
                    await log.info(f"没有匹配到对应任务 {tg_text}")
                    return
                urllib = await self.va_url(select, tg_list)
                if urllib[0]:
                    for url in urllib[1]:
                        if not await self.repeat(url):
                            return
                        export_va = await self.convert_url([url])
                        # 下面就是加入队列了
                        if export_va:
                            await self.forward(url)
                            await log.info(f"加入队列  {export_va}")
                            await queue.put([export_va[0].js_level, export_va])
                else:
                    export_va = ExportModel.from_orm(urllib[1][0])
                    # 这里缺失链接
                    export_va.value = urllib[1]
                    await self.forward(urllib[1])
                    await log.info(f"加入队列 {[export_va]}")
                    await queue.put([export_va.js_level, [export_va]])
                return
        except Exception as e:
            await log.debug(f"异常 {e} 触发异常内容 {text}")

    async def convert_url(self, https: list[str]) -> list[ExportModel]:
        """
        url转换成活动
        :param https:
        :type https:
        :return:
        :rtype:
        """
        export_mo = []
        for i in https:
            activ_list = await self.contains_url(i)
            for activ in activ_list:
                # 对活动类型进行判断
                TYPE = re.findall("https://(\w{2})", i)[0]
                if activ.type_url not in [None, TYPE]:
                    continue
                re_expo = re.findall(activ.re_url, i)
                if re_expo:
                    exp = ExportModel.from_orm(activ)
                    if not activ.value2:
                        # 对那些需要两个组成一个
                        if activ.cutting and type(re_expo[0]) != str:
                            exp.value = f'{activ.value1}="{re_expo[0][0]}{activ.cutting}{re_expo[0][0]}";'
                        else:
                            exp.value = f'{activ.value1}="{re_expo[0]}";'
                    elif not activ.value3:
                        exp.value = f'{activ.value1}="{re_expo[0][0]}";{activ.value2}="{re_expo[0][1]}";'
                    else:
                        exp.value = f'{activ.value1}="{re_expo[0][0]}";{activ.value2}="{re_expo[0][1]}";{activ.value3}="{re_expo[0][2]}";'
                    export_mo.append(exp)
        return export_mo

    async def forward(self, text):
        """
        转发消息
        :param text:
        :type text:
        :return:
        :rtype:
        """
        for chat_id in self.chat_id_list:
            await self.bot.send_message(chat_id=chat_id, disable_web_page_preview=True, text=text)

    async def repeat(self, text: str) -> bool:
        """
        用来检测是否执行的
        :param text:
        :type text:
        :return:
        :rtype:
        """
        # 如果超过时间则删除
        if self.expired < int(time.time()):
            await self.dele_ti(int(time.time()))
            self.expired = int(time.time()) + 3600
        # 检测是否存在
        re_per = re.findall("(?:activityId=|configCode=|actId=|code=|token=|shopId=|id=)(\w+)&?", text)
        if re_per:
            async with self.lock:
                se_re = await self.select_pe(value=re_per[0])
                if se_re:
                    await log.info(f"{re_per[0]} 已经执行过了")
                    return False
                else:
                    await self.add_pe(value=re_per[0], time=int(time.time()) + 3600)
                    return True
        else:
            await log.info(f"检测执行正则匹配失败, {text}")
            return False
