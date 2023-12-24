import aiogram

from aiogram import types, Dispatcher, Bot, Router
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.filters import and_f

from core.points import Points
from init.conf import conf
from utils.logs import log

black_id = conf.tg.black_id + conf.tg.forward_from
# All handlers should be attached to the Router (or Dispatcher)
router = Router()
poni = Points()


@router.message(and_f(aiogram.F.chat.type == 'private', aiogram.F.text))
async def private_handler(message: types.Message) -> None:
    """
    接收私聊消息和文本
    """
    try:
        if message.forward_from_chat:
            text = f"用户信息\n" \
                   f"你的id:  {message.chat.id}\n" \
                   f"你的名字: {message.chat.first_name if message.chat.first_name else ''}{f' {message.chat.last_name}' if message.chat.last_name else ''}\n" \
                   f"转发内容相关\n" \
                   f"转发id: {message.forward_from_chat.id}\n" \
                   f"转发名称: {message.forward_from_chat.title}"
            await message.answer(text=text)
        await poni.pie(message.text)
    except TypeError:
        await message.answer("Nice try!")


@router.message(and_f(aiogram.F.chat.type != 'private', aiogram.F.text))
async def private_handler(message: types.Message) -> None:
    """
    接收非私聊消息和文本,主要用于监控活动大概
    """
    try:
        # 屏蔽转发的id和转发群组的ID
        if message.forward_from_chat and message.forward_from_chat.id in black_id:
            await log.debug(f"{message.forward_from_chat.id} 设置了屏蔽或转发将自动屏蔽该内容")
        elif message.chat.id in black_id:
            await log.debug(f"{message.chat.id} 设置了屏蔽或转发将自动屏蔽该内容")
        else:
            await poni.pie(message.text)
    except TypeError:
        await message.answer("Nice try!")


async def main_bot() -> None:
    await log.info(f"欢迎使用 aigramBot {conf.project.Identity} {conf.project.Version}")
    # Bot token can be obtained via https://t.me/BotFather
    if conf.tg.tg_proxy:
        session = AiohttpSession(proxy=conf.tg.tg_proxy)
        await log.info("代理了TG的域名")
    elif conf.tg.tg_api:
        session = AiohttpSession(
            api=TelegramAPIServer.from_base(conf.tg.tg_api)
        )
        await log.info("使用不安全反代连接TG")
    else:
        session = None
        await log.info("使用直连进行连接TG")

    # logging.basicConfig(level="INFO")
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(conf.tg.bot_token, parse_mode="HTML", session=session)
    poni.bot = bot
    a = await bot.get_me()
    if not a.can_join_groups:
        await log.error("无法加入群组 找 https://t.me/BotFather 发送 /setjoingroups 选择 @{a.username} 选择 Enable")
    if not a.can_read_all_group_messages:
        await log.error(f"无法接收全部消息 找 https://t.me/BotFather 发送 /setprivacy 选择 @{a.username} 选择 DISABLED")
    await log.info(f"机器人名称: @{a.username} 已经上线")
    # And the run events dispatching
    await dp.start_polling(bot, polling_timeout=100)
