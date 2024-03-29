import asyncio

from init.conf import log
from bot.bot import main_bot
from core.run import Core
from db.db_init import init

cores = Core()


async def main():
    # 配置日志
    await log.info("配置文件加载成功开始执行")
    await init()
    await log.info("本项目地址 https://github.com/XgzK/aigramBot")
    await log.info("本项目仅仅是 QL_variable 的重写版本")
    await log.info("本项目不对任何ck泄漏负责,使用本项目默认允许偷取行为存在")
    await log.info("如果你使用本项目建议加TG https://t.me/InteTU 频道所属私有群 或 https://t.me/InteIJS 获取详细使用说明")
    await log.info("本项目所有线报来源如下群或者频道 https://t.me/InteTU/163")
    await asyncio.gather(main_bot(), cores.die_while())


if __name__ == '__main__':
    asyncio.run(main=main())
