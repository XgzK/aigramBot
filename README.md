# aigramBot
[![Telegram Bot API](https://img.shields.io/badge/dynamic/json?color=blue&logo=telegram&label=Telegram%20Bot%20API&query=%24.api.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Faiogram%2Faiogram%2Fdev-3.x%2F.butcher%2Fschema%2Fschema.json&style=flat-square)](https://core.telegram.org/bots/api)

本项目基于 [aiogram](https://docs.aiogram.dev/en/dev-3.x/contributing.html) 开发,后续会添加 [FastAPI](https://fastapi.tiangolo.com/) 的Web部分功能
本项目主要基于TGBot监控频道和群的线报配合青龙执行对应脚本任务

### TGBot缺陷和好处
缺陷
```text
无法加入禁止bot身份加入的群
普通用户无法邀请机器人加入频道
一个群组最多只能存在20个机器人
相对人形 傻妞 spy 无界 等人形机器人限制相对较大
```
好处
```text
TGBot是官方推出机器人相对人形 傻妞 spy 无界 等人形机器人等封号风险问题将不会存在
申请简单
可能这是TGBot为数不多的优点之一吧
```
### 警告
在开发者不同意情况下禁止设置转发
当然如果你希望本项目尽快删库跑路可以尽情转发
如果发现未经开发者允许转发者，将会私有项目不再对外提供任何服务
当然写这么多还是会有人私自转发,在 [QL_variable](https://github.com/XgzK/QL_variable) 项目中就发现了多个私自设置转发的，也被监控群组的管理者告知不能监控的谈话，希望使用者尽情作死，让本人早日结束漫长的维护过程,不要觉得因为这个项目有任何收益情况，到现在为止解析短链每个月都需要耗费6元代理费用，而每月豆子还达不到6元收益,负收入开发中，当然说这么多不是在对你们哭穷，只是告诉你们如果删除项目会更有益，也会节省更多时间去打打游戏也好找小姐姐聊天也好都比维护这种没技术含量的项目强
```shell
docker run -dit \
  -e TZ=Asia/Shanghai \
  --name aigramBot \
  --restart unless-stopped \
  xgzk/aigrambot:test
```

### 对接青龙
进入青龙容器
```text
青龙10版本执行
touch /ql/config/qlva.sh
青龙11以后执行
touch /ql/data/config/qlva.sh

青龙面板 修改配置文件 config.sh
10添加 source /ql/config/qlva.sh
11以后添加 source /ql/data/config/qlva.sh
可以在配置文件的文件看到qlva.sh文件
```
### aigramBot配置
#### 完整配置
进入服务器
```shell
touch config.json5 // 创建文件 config.json5
vim config.json5 // 打开文件,把对应配置复制进去填写
docker cp config.json5 aigramBot:/aigram
```
```json5
{
  "tg": { // tg相关
    "user_id": "", //个人id 没有实现
    "bot_token": "", // 机器人token 必填
    "tg_api": "",// 反代如果国内填写
    "tg_proxy": "", // 代理 socks5://127.0.0.1:10808
    "forward_from": [ // 转发ID 设置转发会自动屏蔽转发的ID
      -100123456789,
      12456777
    ],
    "black_id": [ // 屏蔽ID
      -1001246788,
      12456777
    ]
  },
  "activities": {// 活动相关
    "black_keywords": [ // 屏蔽的活动关键字
      "activityId",
      "id1&id2"
    ],
    "black_script": [ // 屏蔽脚本
      "jd_opencardL309.js",
      "jd_tj_cxjhelp.js"
    ]
  },
  "ql": {
    "file": "qlva.sh", // 写入青龙的文件,不能使用青龙自带的文件
    "url": "",// 青龙的地址 http://ip:post 不带/
    "Client_ID": "", // 青龙面板 系统变量 应用设置 
    "Client_Secret": "" // 需要权限 定时任务 配置文件
  },
  "project": {
    "log_level": "INFO", // 日志打印级别 普通用户不用修改
    "log_path": "logs/", // 日志存储路径
    "interval": 5 // 脚本执行完毕停止秒数默认5秒
  }
}
```

# 线报配置
```text
match_url 教程
    表示拼接成的链接 如 export jd_txzj_sign_in_id 拼接的head_url是 https://txzj-isv.isvjcloud.com/sign_in/home?a=jd_txzj_sign_in_id
re_url 
    (https.*?activityType=(?:10020|10021|10026|10031|10063|10080).*) 匹配链接有 10020 10021 10026 10031 10063 10080 其中一个出现就匹配 
    (https.*?activityType=10024.*) 匹配 activityType=10024
head_url 
   匹配正则表达式 com/((?:ql/|microDz/)?[a-zA-Z]+/?[a-zA-Z]*) 匹配结构去掉com/ 去在线正则表达式测试就看到了
```
```json5
{
  "alias": "脚本的中文名称", // 必填
  "name": "脚本的名称 sh js py", // 必填
  "match_url": "活动转url使用的,通常是export转链接的拼接",
  "re_url": "url转活动的正则表达式",
  "head_url": "链接关键部分", // 
  "type_url": "脚本支持链接类型",
  "cutting": "拼接符号",
  "delays": "间隔秒", // 默认5
  "js_level": 5,// 脚本优先所有脚本优先级 0最高往后优先级别越来越低
  "level": "脚本优先级别越大级别越高",// 默认0
  "value1": "export jd_1", // 必填
  "value2": "export jd_2",
  "value3": "export jd_3",
}
```
下面是必填否则报错
```json5
{
  "alias": "脚本的中文名称", // 必填
  "name": "脚本的名称 sh js py", // 必填
  "value1": "export jd_1", // 必填
}
```
演示
```json5
{
  "alias": "关注店铺有礼（超级无线欧莱雅）",
  "name": "jd_lzkj_loreal_lkFollowShop.js",
  "match_url": "jd_lzkj_loreal_lkFollowShop_ur",
  "re_url": "(https.*?activityType=10069.*?activityId=\\w+.*?)",
  "head_url": "prod/cc",
  "value1": "export jd_lzkj_loreal_lkFollowShop_ur"
}
```
```json5
{
  "alias": "积分兑换京豆 · 超级会员",
  "name": "jd_pointExgBeans.js",
  "match_url": "jd_pointExgBeans_activityUrl",
  "re_url": ".*", // 表示匹配链接所有
  "level": 4,
  "head_url": "mc/wxPointShopView/pointExgBeans", 
  "value1": "export jd_pointExgBeans_activityUrl"
}
```
### 版本
- > 0.1 内测版本  
  > 简单实现了 [QL_variable](https://github.com/XgzK/QL_variable) 的功能,没有单个脚本延迟执行, 没有实现web端,没有实现禁用青龙任务,没有实现多青龙面板支持,没有实现远程数据库支持
- > 0.2 内测版本  
  > 修复同时发送相同活动无法过滤bug  
  > 修复同消息多链接遇到执行过活动结束bug  
  > 修复私聊发送活动无法执行问题 
- > 0.3 内测版本  
  > 添加 js_level 队列优先级,优先执行优先级别高的脚本
  > 任务队列实现  
  > interval 参数实现脚本执行下个任务等待时间 默认等待五秒
- > 0.3 内测版本
  >  更正 jd_daily.js jd_drawShopGift.js 