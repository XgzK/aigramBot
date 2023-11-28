import re


from models.activities import Activities


class Convert:

    def __init__(self):
        pass

    async def va_url(self, activ: list[Activities], re_list: list) -> list[str]:
        """
        活动转链接如果成功返回 [url] 如果失败返回 []
        :param activ:
        :type activ:
        :param re_list:
        :type re_list:
        :return: list[str]
        :rtype:
        """
        if not activ[0].match_url:
            st = ""
            for i in re_list:
                st += f'{i[0]}="{i[1]}";'
            return [st]
        # 处理链接中出现#的特殊字段
        re_sp = re.findall("#\d", activ[0].match_url)
        if re_sp:
            sp_li = re_list[0][1].split(activ[0].cutting)
            # 进入这里说明需要拆分
            if len(re_sp) == len(sp_li):
                st = activ[0].match_url
                for i in range(len(re_sp)):
                    st = st.replace(f"#{i}", sp_li[i])
                return [st]

        if not activ[0].value2:
            if activ[0].cutting:
                # 处理店铺签到类似活动值
                url_list = []
                a = str(re_list[0][1]).split(activ[0].cutting)
                for i in a:
                    url_list.append(activ[0].match_url.replace(re_list[0][0].replace("export ", ""), i))
                return url_list

            return [activ[0].match_url.replace(re_list[0][0].replace("export ", ""), re_list[0][1])]
        else:
            st = activ[0].match_url
            for i in re_list:
                st = st.replace(i[0].replace("export ", ""), i[1])
            return [st]

