from django.db import models


class Category(models.Model):
    name = models.CharField('NAME', max_length=20, unique=True, null=False)
    parent = models.ForeignKey('self', related_name="category_child", default=None, null=True, on_delete=models.CASCADE,
                               db_column='parent_id')
    priority = models.SmallIntegerField()

    class Meta:
        db_table = "category_category"

    def __str__(self):
        return f'Category : {self.name}, {self.priority}'
