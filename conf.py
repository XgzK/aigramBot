"""
根据用户选择生成相应配置
让用户输入BOT
问用户是否在国内
    是否使用代理
        请输入代理
    else
        自动配置反代
请输入青龙相关配置
    请输入青龙
设置屏蔽不
"""
import json
import random

conf = {
    "tg": {
        "user_id": "",
        "bot_token": "",
        "tg_api": "",
        "tg_proxy": "",
        "forward_from": [
        ],
        "black_id": [
        ]
    },
    "activities": {
        "black_keywords": [
        ],
        "black_script": [
        ]
    },
    "ql": {
        "url": "",
        "Client_ID": "",
        "Client_Secret": ""
    },
    "project": {
    }
}
tgurl = ["https://tg-bot.0x23.cf"] #, "https://thingproxy.freeboard.io/fetch/https://api.telegram.org"]


def tg():
    """
    tg配置相关
    :return:
    :rtype:
    """
    bot_token = input('请输入你的机器人bot_token: ')
    conf['tg']['bot_token'] = bot_token
    # 环境
    yn = input('你这台机器所在位置是否为国内 是输入 Y 否输入 N: ')
    if yn == "Y":
        pr = input('否使用代理连接TG(推荐使用) 是输入 Y 否输入 N: ')
        if pr == "Y":
            tg_proxy = input('请输入代理 支持 http https socks socks4 socks5 格式 http://ip:post :')
            conf['tg']['tg_proxy'] = tg_proxy
        else:
            print("由于你没有选择使用代理,将会为你自动配置反代域名连接TG")
            conf['tg']['tg_api'] = random.choice(tgurl)

    # 转发
    forward = input('是否需要转发 是输入 Y 否输入 N (未经开发者同意请误随意转发): ')
    if forward == "Y":
        forward_from = input('请输入要转发的ID: ')
        conf['tg']['forward_from'].append(int(forward_from))


def ql():
    # 青龙相关
    url = input('请输入青龙地址 http://ip:post : ')
    conf['ql']['url'] = url
    Client_ID = input('请输入青龙Client_ID : ')
    conf['ql']['Client_ID'] = Client_ID
    Client_Secret = input('请输入青龙Client_Secret : ')
    conf['ql']['Client_Secret'] = Client_Secret


tg()
ql()
with open("config.json5", "w+", encoding="UTF-8") as f:
    json.dump(conf, f, ensure_ascii=False, indent=4, sort_keys=True)
