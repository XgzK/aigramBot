"""
一直死循环执行
"""
import asyncio
import re
import time
from typing import Dict

from pydantic import ValidationError

from core import queue
from db.db_repeats import MethodRepeats
from init.conf import conf, log, activities_model
from models.repeats import Repeats
from schemas.conf import QlModel
from utils.ql import Ql


class Core(Ql, MethodRepeats):

    def __init__(self):
        try:
            self.ql = QlModel.model_validate(conf.ql)
        except ValidationError as exc:
            print("Core 读取出现异常: ", exc.json())
        self.interval = conf.project.interval
        super().__init__()
        self.queue = queue
        self.expired: int = int(time.time()) + 3600
        self.new_time: int = 0  # ql下次任务列表获取时间
        self.ql_json: dict = {}
        self.ql_tf = False
        self.black_script = conf.activities.black_script
        self.Delay_dict = dict()
        MethodRepeats.__init__(self, Repeats)

    async def die_while(self):
        """
        死循环获取队列任务
        :return:
        :rtype:
        """
        # 删除所有数据
        await self.delete_all()
        while True:
            get_queue = await self.queue.get()
            if not get_queue:
                continue
            # 过滤重复
            if not await self.repeat(get_queue):
                continue

            # 对链接进行转换
            name_js = activities_model.Activities(get_queue)
            if not name_js:
                await log.debug(f"没有适配脚本: {get_queue}")
            # 开始执行后续任务
            if not await self.detection():
                continue
            await self.ql_task_run(name_js)
            await asyncio.sleep(2)

    async def detection(self):
        """
        检测是否缺失
        :return:
        :rtype:
        """
        if self.ql.url == "" or not self.ql.url:
            await log.info("填写青龙配置缺失")
            return False
        ti = int(time.time())
        # 先检测是否过期或者或者需要获取青龙的
        if self.ql.expiration <= ti:
            await log.info(f"获取青龙auth 青龙返回有效时间 {self.ql.expiration} 当前时间 {ti}")
            params = {
                'client_id': self.ql.Client_ID,
                'client_secret': self.ql.Client_Secret
            }
            # 如果过期将会重新获取
            ql_tk = await self.token(self.ql.url, params)
            if ql_tk == {} or ql_tk['code'] != 200:
                return False
            # 写入模型中
            self.ql.Authorization = f"{ql_tk['data']['token_type']} {ql_tk['data']['token']}"
            if int(ql_tk['data']['expiration']) > int(time.time()):
                self.ql.expiration = int(ql_tk['data']['expiration'])
            else:
                self.ql.expiration = int(time.time()) + 3600

        # 获取青龙的任务列表
        if self.new_time <= ti:
            await log.info("获取任务列表")
            ql_json = await self.get_crontab_json(url=self.ql.url, auth=self.ql.Authorization)
            if ql_json is None:
                return False
            self.ql_json = ql_json
            self.new_time = ti + 3600
        # 检测青龙配置文件是否存在
        if not self.ql_tf:
            ql_path = await self.get_configs_files(url=self.ql.url, auth=self.ql.Authorization)
            if ql_path['code'] != 200:
                pass
            for file in ql_path['data']:
                if file['title'] == self.ql.file:
                    self.ql_tf = True
                    return True
            await log.error(f"青龙配置文件中没有检测到 {self.ql.file} 文件 请参考说明文档有关青龙设置部分")
            return False
        return True

    async def ql_task_run(self, get_queue: Dict) -> bool:
        """
        执行青龙任务
        :param get_queue:
        :type get_queue:
        :return:
        :rtype:
        """
        # 用于记录没有存在的脚本
        list_js = ""
        for js_queue in get_queue:
            if js_queue in self.black_script:
                await log.info(f"{js_queue} 脚本已被屏蔽")
                continue
            # 监测脚本是否存在
            if js_queue not in self.ql_json:
                list_js += f"{js_queue} "
                continue
                # 获取脚本信息
            name_json = self.ql_json.get(js_queue)
            await log.info(f"开始写入青龙配置文件 执行的脚本: {list(name_json.keys())[0]} 写入值{get_queue[js_queue]}")
            try:
                # 写入配置文件中
                save = await self.post_configs_save(url=self.ql.url, auth=self.ql.Authorization,
                                                    content=get_queue[js_queue], path=self.ql.file)
                if save['code'] != 200:
                    await log.error(f"青龙返回状态码异常 {save}")
                    return False
                run = await self.put_crontab_run(url=self.ql.url, auth=self.ql.Authorization,
                                                 data=[name_json.get(list(name_json.keys())[0])['id']])
                if run['code'] != 200:
                    await log.error(f"青龙返回状态码异常 {run}")
                    return False
                await log.info(f"发送执行命令成功 脚本名称: {list(name_json.keys())[0]} 参数 {get_queue[js_queue]}")
            except Exception as e:
                await log.error(f"执行青龙发送异常: {e}")
            return True
        # 进入这里就是没有找到
        await log.info(f"{list_js} 系列脚本都没有找到")
        return False

    async def repeat(self, text: str) -> bool:
        """
        用来监测是否执行过对应的值过滤重复内容
        :param text:
        :type text:
        :return:
        :rtype:
        """
        # 过滤去重复
        if conf.activities.repeat:
            return True
        # # 如果超过时间则删除
        if self.expired < int(time.time()):
            await self.dele_ti(int(time.time()))
            self.expired = int(time.time()) + 3600
        # 检测是否存在 ，如果是链接则使用正则获取其关键字
        re_per = re.findall("(?:activityId|configCode|actId|code|token|shopId|venderId|id)=(\w+)&?", text)
        if not re_per:
            re_per = re.findall("export [\w_]+=\"?'?([\w:/.\-@&,?=]+)\"?'?", text)
        if not re_per:
            return True

        if re_per:
            se_re = await self.select_pe(value=re_per[0])
            if se_re:
                await log.info(f"{re_per[0]} 已经执行过了")
                return False
            else:
                await self.add_pe(value=re_per[0], time=int(time.time()) + 3600)
                return True
        return True
