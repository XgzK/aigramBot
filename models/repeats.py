from tortoise import Model, fields


class Repeats(Model):
    value = fields.TextField(default=None, null=True, description="指向关键字")
    time = fields.IntField(default=None, null=True, description="删除结束时间")

    class Meta:
        table_description = "执行关键字的表"