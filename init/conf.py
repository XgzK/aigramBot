import json
import os
import time

import aiofiles
import json5

from schemas.conf import ConfModel

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
conf: ConfModel = ConfModel(**data)


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
        return {}


async def write(file: str, data: json):
    """
    写入内容到json覆盖形式
    :param file:
    :type file:
    :param data:
    :type data:
    :return:
    :rtype:
    """
    async with aiofiles.open(file, mode='w+') as f:
        await f.write(json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True))
