"""
一直死循环执行
"""
import asyncio
import time

from core import queue
from init.conf import conf
from schemas.activities import ExportModel
from schemas.conf import QlModel
from utils.logs import log
from utils.ql import Ql

ql = QlModel.from_orm(conf.ql)


class Core(Ql):

    def __init__(self):
        super().__init__()
        self.queue = queue
        self.new_time: int = 0  # ql下次任务列表获取时间
        self.ql_json: dict = {}
        self.ql_tf = False
        self.black_script = conf.activities.black_script

    async def die_while(self):
        """
        死循环获取队列任务
        :return:
        :rtype:
        """
        while True:
            get_queue = await self.queue.get()
            tf = await self.detection()
            if not tf:
                continue
            # 开始执行后续任务
            if ql.url:
                await self.ql_task_run(get_queue)
                await asyncio.sleep(2)
            else:
                await asyncio.sleep(10)

    async def detection(self):
        """
        检测是否缺失
        :return:
        :rtype:
        """
        if ql.url == "" or not ql.url:
            await log.info("填写青龙配置缺失")
            return False
        ti = int(time.time())
        # 先检测是否过期或者或者需要获取青龙的
        if ql.expiration <= ti:
            await log.info("获取青龙auth")
            params = {
                'client_id': ql.Client_ID,
                'client_secret': ql.Client_Secret
            }
            # 如果过期将会重新获取
            ql_tk = await self.token(ql.url, params)
            if ql_tk['code'] != 200:
                return False
            # 写入模型中
            ql.Authorization = f"{ql_tk['data']['token_type']} {ql_tk['data']['token']}"
            ql.expiration = ql_tk['data']['expiration']

        # 获取青龙的任务列表
        if self.new_time <= ti:
            await log.info("获取任务列表")
            self.ql_json = await self.get_crontab_json(url=ql.url, auth=ql.Authorization)
            self.new_time = ti + 3600
        # 检测青龙配置文件是否存在
        if not self.ql_tf:
            ql_path = await self.get_configs_files(url=ql.url, auth=ql.Authorization)
            if ql_path['code'] != 200:
                pass
            for file in ql_path['data']:
                if file['title'] == ql.file:
                    self.ql_tf = True
                    return True
            await log.error(f"青龙配置文件中没有检测到 {ql.file} 文件 请参考说明文档有关青龙设置部分")
            return False
        return True

    async def ql_task_run(self, get_queue: list[ExportModel]) -> bool:
        """
        执行青龙任务
        :param get_queue:
        :type get_queue:
        :return:
        :rtype:
        """
        list_js = ""
        # 遍历活动任务
        for get_list in get_queue:
            # 屏蔽的脚本
            if get_list.name in self.black_script:
                await log.info(f"{get_list.name} 脚本已被屏蔽")
                continue

            # 如果不存在则跳过
            if get_list.name not in self.ql_json:
                list_js += f"{get_list.name} "
                continue
            name_json = self.ql_json.get(get_list.name)
            # 写入配置文件中
            save = await self.post_configs_save(url=ql.url, auth=ql.Authorization, content=get_list.value,
                                                path=ql.file)
            if save['code'] != 200:
                await log.error(f"青龙返回状态码异常 {save}")
                return False
            run = await self.put_crontab_run(url=ql.url, auth=ql.Authorization,
                                             data=[name_json.get(list(name_json.keys())[0])['id']])
            if run['code'] != 200:
                await log.error(f"青龙返回状态码异常 {run}")
                return False
            await log.info(f"执行 {get_list.alias} {get_list.name} 参数 {get_list.value}")
            return True
        # 进入这里就是没有找到
        await log.info(f"{list_js} 系列脚本都没有找到")
        return False
