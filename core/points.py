"""
用于分拣活动
"""
import asyncio
import re
import time

from core import queue
# from core import queue
from db.db_repeats import MethodRepeats
from init.conf import conf, log, jd_url_config
from models.repeats import Repeats


# from utils.queue import QueueItem


class Dispose:
    def __init__(self):
        MethodRepeats.__init__(self, Repeats)
        self.bot = None
        self.chat_id_list: list[int] = conf.tg.forward_from
        self.black_keywords = "|".join(conf.activities.black_keywords)
        self.lock = asyncio.Lock()

    async def pie(self, text: str):
        """
        用于把各种值进行分类，缺陷无法判断同一行中同类型
        :param text:
        :type text:
        :return:
        :rtype:
        """
        try:
            if self.black_keywords:
                if re.findall(f"(?:{self.black_keywords})+", text):
                    await log.debug("屏蔽关键字存在跳过执行")
                    return
            # 对包含的export 关键字进行转换
            for url in jd_url_config.JdUrl_export_list(text):
                #  await queue.put(QueueItem(export_va[0].js_level, export_va))
                await queue.put(url)
                await self.forward(url)
                # t_tx = re.findall(r'(https://[\w\-.]+(?:isv|jd).*?\.com/[a-zA-Z0-9&?=_/-].*)', text)
        except Exception as e:
            await log.debug(f"异常 {e} 触发异常内容 {text}")

    async def forward(self, text):
        """
        如果设置转发会把内容转发出去，并没有对其进行转发失败处理
        :param text:
        :type text:
        :return:
        :rtype:
        """
        if self.chat_id_list:
            for chat_id in self.chat_id_list:
                await self.bot.send_message(chat_id=chat_id, disable_web_page_preview=True, text=text)
