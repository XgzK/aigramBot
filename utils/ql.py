import json
import re

from init.conf import log
from utils.aioclient import HTTPClient


class Ql(HTTPClient):
    def __init__(self):
        super().__init__()
        self.headers = {
            'Accept': 'application/json',
            'Authorization': "",
            'Content-Type': 'application/json;charset=UTF-8'
        }
        self.timeout = 60

    async def token(self, url: str, params: dict) -> dict:
        """
        用于获取登录用的ck,ck有效期一个月
        :param params:
        :type params:
        :param url: 青龙数据库
        :return: 返回登录用的Bearer XXXXXXXXXXX，[状态码,内容]
        {'code': 200, 'data': {'token': '', 'token_type': 'Bearer', 'expiration': 1688216420}}
        {'code': 400, 'message': 'client_id或client_seret有误'}
        {'code': 401, 'message': 'UnauthorizedError'}
        """
        try:
            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json;charset=UTF-8'
            }
            tk = await self.get(url=url + "/open/auth/token", headers=headers, params=params, timeout=6)
            return tk
        except Exception as e:
            await log.error(f"/open/auth/token接口异常: {e}")
            return {}

    async def get_crontab(self, url: str, auth) -> dict:
        """
        获取任务列表
        :param self:
        :type self:
        :param url:
        :type url:
        :param auth:
        :type auth:
        :return:
        :rtype:
        """
        headers = self.headers
        headers["Authorization"] = auth
        tk = await self.get(url=url + "/open/crons", headers=headers)
        return tk

    async def put_crontab_run(self, url: str, auth: str, data: list) -> dict:
        """
        执行任务
        :param url:
        :type url:
        :param auth:
        :type auth:
        :param data: [id]
        :type data:
        :return:
        :rtype:
        """
        headers = self.headers
        headers["Authorization"] = auth
        return await self.put(url=url + "/open/crons/run", headers=headers, data=data)

    async def put_crontab_disable(self, url: str, auth: str, data: list) -> dict:
        """
        禁用任务
        :param url:
        :type url:
        :param auth:
        :type auth:
        :param data: [id]
        :type data:
        :return:
        :rtype:
        """
        headers = self.headers
        headers["Authorization"] = auth
        return await self.put(url=url + "/open/crons/disable", headers=headers, data=data)

    async def get_configs_files(self, url: str, auth) -> dict:
        """
        获取青龙configs文件名称
        :param url:
        :type url:
        :param auth:
        :type auth:
        :return:
        :rtype:
        """
        headers = self.headers
        headers["Authorization"] = auth
        tk = await self.get(url=url + "/open/configs/files", headers=headers)
        return tk

    async def get_configs(self, url: str, path: str, auth) -> dict:
        """
        获取配置文件内容
        :param url:
        :type url:
        :param path: 文件名称
        :type path:
        :param auth:
        :type auth:
        :return:
        :rtype:
        """
        headers = self.headers
        headers["Authorization"] = auth
        tk = await self.get(url=url + "/open/configs/" + path, headers=headers)
        return tk

    async def post_configs_save(self, url: str, auth: str, content: str, path: str) -> dict:
        """
        覆盖文件内容
        :param url:
        :type url:
        :param auth:
        :type auth:
        :param content: new内容
        :type content:
        :param path: 文件
        :type path:
        :return:
        :rtype:
        """
        headers = self.headers
        headers["Authorization"] = auth
        return await self.post(url=url + "/open/configs/save", headers=headers, data={"content": content, "name": path})

    async def get_crontab_json(self, url: str, auth) -> dict:
        """
        对get_crontab二次封装, 返回标准统一的json数据
        :param url:
        :type url:
        :param auth:
        :type auth:
        :return: 返回统一话后的json格式数据
        :rtype:
        """
        crontab = await self.get_crontab(url=url, auth=auth)
        json_ql = {}
        """
        crontab['data'] if 'data' in crontab else crontab
        主要解json使用,因青龙不同版本返回的json有差异性
        比如 10版本是 _id 11版本是 id
        13后几个版本 外边多了层[]
        """
        if crontab["code"] != 200:
            await log.info(f"获取任务列表失败: {json.dumps(crontab)}")
            return None
        for js_list in crontab['data']['data'] if 'data' in crontab['data'] else crontab['data']:

            re_filter = re.findall('task .*?(\w+\.(?:py|js|ts))', js_list['command'])
            if re_filter:
                if not (re_filter[0] in json_ql):
                    json_ql[re_filter[0]] = {}
                # 用来区分 版本json格式差异
                json_ql[re_filter[0]].setdefault(js_list['command'],
                                                 {'id': js_list['id' if 'id' in js_list else '_id'],
                                                  "name": js_list["name"], "isDisabled": js_list["isDisabled"]})
            else:
                print(f" 跳过录入任务: {js_list['command']}")
        return json_ql
