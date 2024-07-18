import re

from pydantic import BaseModel
from typing import List


class Value(BaseModel):
    # export 变量名称
    export: List[str] = None
    # re_url 解析链接
    re_url: str = ''
    # cutting 分割符号
    cutting: str = ''

    def Export_Re_List(self, value: str) -> str:
        # 使用正则表达式
        ex_list = re.findall(self.re_url, value)
        if ex_list:
            if len(ex_list) == 1 and type(ex_list[0]) == str:
                return f'export {self.export[0]}="{ex_list[0]}"'
            if len(ex_list) == 1 and type(ex_list[0]) == dict and self.cutting != '':
                return f'export {ex_list[0]}="{"&".join(ex_list[0][0])}"'


class Activity(BaseModel):
    # alias 脚本别名
    alias: str
    # name 脚本名称
    name: str
    # head_url 活动链接关键部分
    head_url: str = ''
    # value 变量名称
    value: List[Value] = None


class ActivitiesModel(BaseModel):
    activitiesUrl: List[Activity]
    activitiesStr: List[Activity]

    def ActivitiesUrl(self, value: str) -> List[str]:
        export_lists = {}
        for activities in self.activitiesUrl:
            export_list = []
            if activities.head_url in value:
                for values in activities.value:
                    # if values.expor not in export_lists:
                    export_value = values.Export_Re_List(value)
                    if export_value:
                        export_list.append(export_value)
            if export_list:
                export_lists[activities.name] = '\n'.join(export_list)
        return export_lists

    def ActivitiesStr(self, value1: str, value2: str) -> List[str]:
        export_lists = {}
        for activities in self.activitiesStr:
            export_list = []
            for values in activities.value:
                # print(values)
                for export in values.export:
                    if export == value1:
                        export_list.append(f'export {value1}="{value2}"')
            if export_list:
                export_lists[activities.name] = '\n'.join(export_list)
        return export_lists

    def Activities(self, value: str) -> List[str]:
        if "https://" in value:
            return self.ActivitiesUrl(value)
        else:
            ex = re.findall("export ([\w_]+)=\"?'?([\w:/.\-@&,?=]+)\"?'?", value)
            if not ex:
                return None
            if type(ex[0]) == tuple:
                return self.ActivitiesStr(ex[0][0], ex[0][1])
            return None