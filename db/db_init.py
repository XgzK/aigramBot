import os

from tortoise import Tortoise

from init.conf import read
from init.sql import js_sql
from models.activities import Activities


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    tf = os.path.exists("db.sqlite3")
    await Tortoise.init(
        db_url='sqlite://./db.sqlite3',
        timezone="Asia/Shanghai",
        modules={'models': ['models.activities', 'models.repeats']}
    )
    # Generate the schema
    await Tortoise.generate_schemas(safe=True)
    if not tf:
        await enter()


async def enter():
    """
    录入数据库内容
    :return:
    :rtype:
    """
    # 检测有没有sql文件
    if os.path.exists("sql.json"):
        jsql = await read('sql.json')
        if "activities" not in jsql:
            jsql = js_sql
    else:
        jsql = js_sql
    objects = []
    for i in jsql["activities"]:
        objects.append(Activities(**i))
    await Activities.bulk_create(objects=objects)
