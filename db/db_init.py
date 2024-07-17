from tortoise import Tortoise


async def init():
    await Tortoise.init(
        db_url='sqlite://./db.sqlite3',
        timezone="Asia/Shanghai",
        modules={'models': ['models.repeats']}
    )
    await Tortoise.generate_schemas(safe=True)
