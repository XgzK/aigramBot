import os
import sys
from loguru import logger

from init.conf import conf


class AsyncLog:
    def __init__(self, log_path=None, level="INFO"):
        self.log_path = log_path if log_path else "logs/"
        # os.makedirs(self.log_path, exist_ok=True)

        self.logger = logger
        self.logger.remove()
        if level != "INFO":
            self.logger.add(
                sink=sys.stdout,
                format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <magenta>aigramBot</magenta> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
                level=level,
                enqueue=True,
            )
        else:
            self.logger.add(
                sink=sys.stdout,
                # | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>
                format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <magenta>aigramBot</magenta> | <level>{level}</level> - <level>{message}</level>",
                level=level,
                enqueue=True,
            )

        # self.logger.add(
        #     sink=os.path.join(self.log_path, "{time:YYYY-MM-DD}.log"),
        #     format="{time:YYYY-MM-DDTHH:mm:ss} | aigramBot | {level} | {name}:{function}:{line} - {message}",
        #     rotation="00:00",
        #     retention="7 days",
        #     # compression="zip",
        #     level=level,
        #     encoding="utf-8",
        #     enqueue=True
        # )

    async def info(self, message):
        self.logger.opt(depth=1, exception=False).info(message)
        await logger.complete()

    async def debug(self, message):
        self.logger.opt(depth=1, exception=False).debug(message)
        await logger.complete()

    async def warn(self, message):
        self.logger.opt(depth=1, exception=False).warning(message)
        await logger.complete()

    async def error(self, message):
        self.logger.opt(depth=1, exception=False).error(message)
        await logger.complete()

    async def exception(self, message):
        self.logger.opt(depth=1, exception=False).exception(message)
        await logger.complete()


log = AsyncLog(level=conf.project.log_level, log_path=conf.project.log_path)
