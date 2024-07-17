import os
import signal
import sys

import aiogram

from aiogram import types, Dispatcher, Bot, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.enums import ParseMode
from aiogram.filters import and_f
from python_socks import ProxyConnectionError

from core.points import Dispose
from init.conf import conf, log

router = Router()
# 处理文本的类
dispose = Dispose()


@router.message(and_f(aiogram.F.chat.type == 'private', aiogram.F.text))
async def private_handler(message: types.Message) -> None:
    """
    接收私聊消息和文本
    """
    try:
        if "/Restart" == message.text:
            os.kill(os.getpid(), signal.SIGINT)
        if "/leave" in message.text:
            await dispose.bot.leave_chat(message.text.split(" ")[1])
        # 如果是转发的消息会返回转发频道有关的信息
        if message.forward_from_chat:
            text = f"用户信息\n" \
                   f"你的id:  {message.chat.id}\n" \
                   f"你的名字: {message.chat.first_name if message.chat.first_name else ''}{f' {message.chat.last_name}' if message.chat.last_name else ''}\n" \
                   f"转发内容相关\n" \
                   f"转发id: {message.forward_from_chat.id}\n" \
                   f"转发名称: {message.forward_from_chat.title}"
            await message.answer(text=text)
        await dispose.pie(message.text)
    except TypeError:
        await message.answer("Nice try!")


@router.message(and_f(aiogram.F.chat.type != 'private', aiogram.F.text))
async def public_handler(message: types.Message) -> None:
    """
    接收公共消息和文本,主要用于监控活动大概
    """
    try:
        if "/leave" in message.text:
            await dispose.bot.leave_chat(message.chat.id)
        # 屏蔽转发的id和转发群组的ID
        if message.forward_from_chat and message.forward_from_chat.id in conf.tg.black_id + conf.tg.forward_from:
            await log.debug(f"{message.forward_from_chat.id} 设置了屏蔽或转发将自动屏蔽该内容")
        elif message.chat.id in conf.tg.black_id + conf.tg.forward_from:
            await log.debug(f"{message.chat.id} 设置了屏蔽或转发将自动屏蔽该内容")
        else:
            await dispose.pie(message.text)
    except TypeError:
        await message.answer("Nice try!")

async def main_bot() -> None:
    await log.info(f"欢迎使用 aigramBot {conf.project.Identity} {conf.project.Version}")
    # Bot token can be obtained via https://t.me/BotFather
    if conf.tg.tg_proxy:
        session = AiohttpSession(proxy=conf.tg.tg_proxy)
        await log.info("代理了TG的域名")
    elif conf.tg.tg_api:
        session = AiohttpSession(api=TelegramAPIServer.from_base(conf.tg.tg_api))
        await log.info("使用不安全反代连接TG")
    else:
        session = None
        await log.info("使用直连进行连接TG")

    dp = Dispatcher()

    dp.include_router(router)
    dispose.bot = Bot(conf.tg.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML), session=session)
    try:
        a = await dispose.bot.get_me()
        if not a.can_join_groups:
            await log.error("无法加入群组 找 https://t.me/BotFather 发送 /setjoingroups 选择 @{a.username} 选择 Enable")
        if not a.can_read_all_group_messages:
            await log.error(f"无法接收全部消息 找 https://t.me/BotFather 发送 /setprivacy 选择 @{a.username} 选择 DISABLED")
        await log.info(f"机器人名称: @{a.username} 已经上线")
        # 启动时候发送基础通知
        if conf.tg.user_id:
            await dispose.bot.send_message(conf.tg.user_id, """支持库
<a href="https://github.com/shufflewzc">faker系列</a> <a href="https://t.me/scriptalking">频道</a> <a href="https://t.me/Soucetalk">群</a>
<a href="https://github.com/feverrun/my_scripts">环境</a> <a href="https://t.me/proenvc">频道</a> <a href="https://t.me/proenv">群</a>
<a href="https://github.com/9Rebels/jdmax">9Rebels</a>
<a href="https://github.com/6dylan6/jdpro">6dylan6</a> <a href="https://t.me/dylan_jdpro">频道</a> <a href="https://t.me/+FrLpTZlvRa4zYTY1">群</a>
<a href="https://github.com/HarbourJ/HarbourToulu">HarbourToulu</a> <a href="https://t.me/HarbourToulu">频道</a> <a href="https://t.me/HarbourChat">群</a>
/Restart 私发给机器人可以重启机器人
/leave 群ID 私发可以退出群聊""")
        elif conf.tg.forward_from:
            for chat in conf.tg.forward_from:
                await dispose.bot.send_message(chat, """支持库
<a href="https://github.com/shufflewzc">faker系列</a> <a href="https://t.me/scriptalking">频道</a> <a href="https://t.me/Soucetalk">群</a>
<a href="https://github.com/feverrun/my_scripts">环境</a> <a href="https://t.me/proenvc">频道</a> <a href="https://t.me/proenv">群</a>
<a href="https://github.com/9Rebels/jdmax">9Rebels</a>
<a href="https://github.com/6dylan6/jdpro">6dylan6</a> <a href="https://t.me/dylan_jdpro">频道</a> <a href="https://t.me/+FrLpTZlvRa4zYTY1">群</a>
<a href="https://github.com/HarbourJ/HarbourToulu">HarbourToulu</a> <a href="https://t.me/HarbourToulu">频道</a> <a href="https://t.me/HarbourChat">群</a>
/Restart 私发给机器人可以重启机器人
/leave 群ID 私发可以退出群聊""")
    except ProxyConnectionError as e:
        await log.error(f"无法链接到网络: {e}")
        sys.exit(1)
    # And the run events dispatching
    await dp.start_polling(dispose.bot, polling_timeout=100)
