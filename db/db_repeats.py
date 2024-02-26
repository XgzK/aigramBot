from init.conf import log
from models.repeats import Repeats


class MethodRepeats:
    def __init__(self, model):
        self.model = model

    async def select_pe(self, value) -> list[Repeats]:
        """
        查询 关键字
        :param value:
        :type value:
        :return:
        :rtype:
        """
        return await self.model.filter(value=value)

    async def add_pe(self, value, time):
        """
        添加
        :param value:
        :type value:
        :param time:
        :type time:
        :return:
        :rtype:
        """
        await Repeats.create(value=value, time=time)

    async def dele_ti(self, times: int) -> int:
        """
        删除超过一定时间的数据
        :param times:
        :type times:
        :return:
        :rtype:
        """
        try:
            return await Repeats.filter(time__gt=times).delete()
        except Exception as e:
            await log.error(e)
            return 0
