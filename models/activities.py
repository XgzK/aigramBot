from tortoise import Model, fields


class TimestampMixin:
    created_at = fields.DatetimeField(null=True, auto_now_add=True, description="创建时候记录")
    modified_at = fields.DatetimeField(null=True, auto_now=True, description="修改更新记录")


class Activities(Model, TimestampMixin):
    id = fields.IntField(pk=True)
    alias = fields.TextField(null=True, description="脚本别名")
    name = fields.CharField(max_length=128, unique=True, null=True, description="脚本名称")

    match_url = fields.TextField(default=None, null=True, description="活动转url使用的")
    re_url = fields.TextField(default=None, null=True, description="url转活动的正则表达式")

    head_url = fields.CharField(default=None, null=True, max_length=50, index=True, description="链接?前面关键字部分")
    type_url = fields.CharField(default=None, null=True, max_length=10, description="活动类型 ls cj 不填写默认所有")
    cutting = fields.TextField(default=None, null=True, description="一些值需要用_@&|切割")

    delays = fields.IntField(default=5, null=True, index=True, description="间隔秒数")
    level = fields.IntField(default=0, null=True, description="优先级")
    js_level = fields.IntField(default=5, null=True, description="脚本优先级")

    value1 = fields.TextField(null=True, description="脚本参数1")
    value2 = fields.TextField(default=None, null=True, description="脚本参数2")
    value3 = fields.TextField(default=None, null=True, description="脚本参数3")

    class Meta:
        table_description = "活动有关的表"
