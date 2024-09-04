import re
from typing import List, Dict

from pydantic import BaseModel


class UrlConfig(BaseModel):
    # 链接模板
    url: str = None
    # 分割符号
    cutting: List[str] = None
    # 是否 #1 方式填补
    urlStr: bool = False

    splicing: List[str] = []

    def UrlStr(self, exoprt_js: List[tuple]) -> List[str]:
        """
        :param exoprt_js:  List[tuple(str, str)]
        :type exoprt_js: 传递{"export" : "值"}
        :return:
        :rtype:
        """
        if (exoprt_js[0][0].endswith("url") or exoprt_js[0][0].endswith("Url")) and len(exoprt_js) == 1:
            # 直接返回链接
            return [exoprt_js[0][1]]
        elif (exoprt_js[0][0].endswith("urls") or exoprt_js[0][0].endswith("Urls")) and len(self.cutting) > 0:
            # 包含多个链接并且设置了分割符号
            for i in self.cutting:
                exoprt_list = exoprt_js[0][1].split(i)
                if len(exoprt_list) > 1:
                    return exoprt_list
                else:
                    return exoprt_js[0][1].split(self.cutting[0])
                return
            return ""
        elif self.splicing:
            textStr = self.url
            # 如果有多个则替换
            for i in exoprt_js:
                textStr = textStr.replace(i[0], i[1])
            return [textStr]
        elif self.cutting:
            # 如果链接有两个地方填补，但是是一个变量 export jd_joinCommonId="1a12ee7043694bb18bc2cac04a6581c5&1000003443"
            # 对变量进行分割
            textList = list()
            # 检测是否存在标记物品
            if not re.findall(f"{''.join(self.cutting)}+", exoprt_js[0][1]):
                 # 如果不操作则返回转换后的
                return [self.url.replace(exoprt_js[0][0], exoprt_js[0][1])]
            for i in self.cutting:
                textStr = self.url
                if self.urlStr:
                    # 如果单个变量填补多个进入
                    exoprt_list = exoprt_js[0][1].split(i)
                    if len(exoprt_list) > 1:
                        for j in range(len(exoprt_list)):
                            textStr = textStr.replace(f"#{j}", exoprt_list[j])
                        textList.append(textStr)
                else:
                    exoprt_list = exoprt_js[0][1].split(i)
                    if len(exoprt_list) > 1:
                        for j in exoprt_list:
                            # 如果分割符号后分割为空跳过
                            if j == "":
                                continue
                            textList.append(textStr.replace(exoprt_js[0][0], j))
            return textList
        else:
            textStr = self.url
            return [textStr.replace(exoprt_js[0][0], exoprt_js[0][1])]


class JdUrl(BaseModel):
    JdUrl: Dict[str, UrlConfig]

    def JdUrl_export_list(self, exoprt_js: str) -> List[str]:

        ex = re.findall("export ([\w_]+)=\"?'?([\w:/.\-@&,?=]+)\"?'?", exoprt_js)
        if not ex:
            if "https://" in exoprt_js:
                return [exoprt_js]
            return []
        if type(ex[0]) == tuple and ex[0][0] in self.JdUrl:
            return self.JdUrl[ex[0][0]].UrlStr(ex)
        elif ex[0][0].endswith("_url"):
            return [ex[0][1]]
        elif "https://" in ex[0][1]:
            return [ex[0][1]]
        return [exoprt_js]