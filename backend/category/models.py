from django.db import models


class Category(models.Model):
    name = models.CharField('NAME', max_length=20, null=False)
    parent_no = models.ForeignKey('self', to_field='id', default=None, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "category_categorys"

    def __str__(self):
        return f'Category : {self.name}'
