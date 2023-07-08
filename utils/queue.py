from schemas.activities import ExportModel


class QueueItem:
    def __init__(self, priority: int, value: list[ExportModel]):
        self.priority = priority
        self.value = value

    def __lt__(self, other):
        # 自定义比较优先级的逻辑
        return self.priority < other.priority