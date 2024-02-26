from schemas.activities import ExportModel


class QueueItem:
    def __init__(self, priority: int, value: list[ExportModel]):
        """
        队列根据设置的优先级进行出站
        :param priority:
        :type priority:
        :param value:
        :type value:
        """
        self.priority = priority
        self.value = value

    def __lt__(self, other):
        # 自定义比较优先级的逻辑
        return self.priority < other.priority
