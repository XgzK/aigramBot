import re

from tortoise.expressions import Q

from init.conf import log
from models.activities import Activities

"""
封装的一些活动库有关的方法
"""


class MethodActivities:
    def __init__(self, models):
        self.models = models

    async def or_select(self, export_va) -> list[Activities]:
        """
        或查询 value1 value2 value3 字段
        :param export_va:
        :type export_va:
        :return:
        :rtype:
        """
        return await self.models.filter(Q(value1=export_va) | Q(value2=export_va) | Q(value3=export_va)).order_by("-level")

    async def contains_url(self, url: str) -> list[Activities]:
        """
        对链接进行模糊匹配多个活动
        :param url:
        :type url:
        :return:
        :rtype:
        """
        re_lis: list[str] = re.findall("com/((?:ql/|microDz/)?[a-zA-Z]+/?[a-zA-Z]*)/", url)
        if not re_lis:
            return []
        try:
            if "prod/cc" in re_lis[0]:
                event = await self.models.filter(Q(re_url__contains=re.search(r'activityType=(\d+)', url).group(1))).order_by("-level")
            else:
                event = await self.models.filter(Q(head_url__contains=re_lis[0])).order_by("-level")
            return event
        except Exception as e:
            await log.error(e)
            return []
