from django.db import models

from category.models import Category


class Item(models.Model):
    name = models.CharField('NAME', max_length=20, null=False)
    reg_date = models.DateTimeField('REG DATE', auto_now_add=True, null=False)
    price = models.SmallIntegerField('PRICE', null=False)
    display = models.BooleanField(null=False)
    stock = models.BooleanField('STOCK', null=False)
    file_url = models.URLField('FILE URL', null=False)
    image_url = models.URLField(null=False)
    category_id = models.ForeignKey(Category, to_field='id', null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "item_items"

    def __str__(self):
        return f'Item : {self.name}'
