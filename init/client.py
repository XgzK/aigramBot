import aiohttp


async def country():
    """
    初始化获取获取位置信息来判断是否需要直连
    :return: CN US 如果异常等问题将会返回 CN
    :rtype:
    """
    try:
        async with aiohttp.ClientSession(base_url="https://ipinfo.io", headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"}) as session:
            async with session.get('/json') as response:
                count = await response.json()
                return count["country"]
    except:
        return "CN"
