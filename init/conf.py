import json
import os
import time

import aiofiles

from schemas.conf import ConfModel

while not os.path.exists("config.json5"):
    print("没有检测到文件存在请按照下面提示操作")
    print("docker exec -i -t aigramBot /bin/sh")
    print("python3 conf.py")
    print("根据提示完成配置")
    time.sleep(10)
if os.path.exists("configtest.json5"):
    conf: ConfModel = ConfModel.parse_file("configtest.json5")
else:
    conf: ConfModel = ConfModel.parse_file("config.json5")


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
