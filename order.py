from tortoise import Tortoise, fields, models


class Order(models.Models):
    order_id = fields.IntField(pk=True)
    order_name = fields.CharField(max_length=100)
    order_price = fields.FloatField()
