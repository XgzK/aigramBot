"""
一直死循环执行
"""
import asyncio
import time

from pydantic import ValidationError

from core import queue
from init.conf import conf
from schemas.activities import ExportModel
from schemas.conf import QlModel
from utils.logs import log
from utils.ql import Ql
from utils.queue import QueueItem
try:
    ql = QlModel.model_validate(conf.ql)
except ValidationError as exc:
    print(exc.json())
interval = conf.project.interval


class Core(Ql):

    def __init__(self):
        super().__init__()
        self.queue = queue
        self.new_time: int = 0  # ql下次任务列表获取时间
        self.ql_json: dict = {}
        self.ql_tf = False
        self.black_script = conf.activities.black_script
        self.Delay_dict = dict()

    async def die_while(self):
        """
        死循环获取队列任务
        :return:
        :rtype:
        """
        while True:
            get_queue = await self.queue.get()
            if not get_queue:
                continue
            t = await self.js_delay(get_queue.value)
            if t:
                # tf = await self.detection()
                # if not tf:
                #     continue
                # 开始执行后续任务
                await self.ql_task_run(get_queue.value)
                await asyncio.sleep(interval)
            elif self.queue.qsize() < 10:
                await asyncio.sleep(interval)
            else:
                await asyncio.sleep(5)


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
        # 用于记录没有存在的脚本
        list_js = ""
        # 遍历活动任务
        for get_list in get_queue:
            # 屏蔽的脚本
            if get_list.name in self.black_script:
                await log.info(f"{get_list.name} 脚本已被屏蔽")
                continue

            # 如果不存在则跳过
            if get_list.name not in self.ql_json:
                list_js += f"{get_list.name}"
                continue
            # 获取脚本信息
            name_json = self.ql_json.get(get_list.name)
            await log.info(f"开始写入青龙配置文件: 写入值{get_list.value} 执行的脚本: {name_json}")
            try:
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
                await log.info(f"发送执行命令成功 活动名称: {get_list.alias} 脚本名称: {get_list.name} 参数 {get_list.value}")
            except Exception as e:
                await log.error(f"执行青龙发送异常: {e}")
            return True
        # 进入这里就是没有找到
        await log.info(f"{list_js} 系列脚本都没有找到")
        return False

    async def js_delay(self, get_queue: list[ExportModel]) -> bool:
        """
        延迟队列,如果时间没到将会让脚本延迟回去等待
        :return:
        :rtype:
        """
        if get_queue[0].name not in self.Delay_dict:
            # 如果没有存在则添加
            self.Delay_dict.setdefault(get_queue[0].name, int(time.time()) + int(get_queue[0].delays))
        else:
            if self.Delay_dict.get(get_queue[0].name) > int(time.time()):
                await log.info(f"此任务才执行没多久需回去排队等待: {get_queue}")
                await self.queue.put(QueueItem(5, get_queue))
                return False

        self.Delay_dict[get_queue[0].name] = int(time.time()) + int(get_queue[0].delays)
        return True

