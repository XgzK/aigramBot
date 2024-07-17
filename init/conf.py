import json
import os
import time

import aiofiles
import json5
from pydantic import ValidationError

from schemas.activities import ActivitiesModel
from schemas.conf import ConfModel
from schemas.url import JdUrl
from utils.logs import AsyncLog

while True:
    if os.path.exists("config.json5") or os.path.exists("/root/config.json5"):
        break
    print("没有检测到文件存在请按照下面提示操作\n"
          "docker exec -i -t aigramBot /bin/sh\n"
          "chmod 777 conf-arm conf-amd \n"
          "选择你架构执行对应架构配置生成\n"
          "./conf-arm\n"
          "根据提示完成配置")
    time.sleep(20)
if os.path.exists("/root/config.json5"):
    with open("/root/config.json5", "r", encoding="utf8") as f:
        data = json5.load(f)
else:
    with open("config.json5", "r", encoding="utf8") as f:
        data = json5.load(f)
conf = ConfModel(**data)
log = AsyncLog(level=conf.project.log_level, log_path=conf.project.log_path)

with open("activity.json", "r", encoding="utf8") as f:
    activity_data = json.load(f)
try:
    activities_model = ActivitiesModel(**activity_data)
except ValidationError as e:
    print(e)

with open("url.json", "r", encoding="utf8") as f:
    dataStr = json.load(f)

# 创建 JdUrl 实例
try:
    jd_url_config = JdUrl(**dataStr)
except ValidationError as e:
    print(e)


async def read(file: str) -> json:
    """
    用于读取文件内容
    :param file:
    :type file:
    :return: 异常返回 {}
    :rtype:
    """
    try:
        async with aiofiles.open(file=file, mode='r', encoding="utf-8") as f:
            contents = await f.read()
        return json.loads(contents)
    except Exception as e:
        print("read 出现异常: ", e)
        return {}
