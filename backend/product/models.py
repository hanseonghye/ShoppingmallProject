from django.db import models

from category.models import Category


class Product(models.Model):
    name = models.CharField('Name', max_length=30, null=False)
    price = models.SmallIntegerField('Price')
    category = models.ForeignKey(Category, to_field='id', on_delete=models.CASCADE)

    stock = models.BooleanField('Stock')
    display = models.BooleanField('Display')

    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify_Date', auto_now=True)

    file_url = models.TextField()
    image_url = models.TextField()

    class Meta:
        db_table = "product_product"

    def __str__(self):
        return f'Category : {self.name}'


class ProductDetail(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=30)
    price = models.SmallIntegerField('Price')
    stock = models.SmallIntegerField('Stock')
    product = models.ForeignKey(Product, to_field='id', null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "product_product_detail"

    def __str__(self):
        return f'ProductDetail : {self.no}, {self.name}, {self.product.name}'


class Option(models.Model):
    name = models.CharField(max_length=30, null=False)
    product = models.ForeignKey(Product, to_field='id', null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "product_option"

    def __str__(self):
        return f'Option : {self.name}, {self.product}'


class OptionDetail(models.Model):
    name = models.CharField(max_length=30, null=False)
    option = models.ForeignKey(Option, to_field='id', null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "product_option_detail"

    def __str__(self):
        return f'OptionDetail : {self.name}, {self.option.name} , {self.option.procudt.name}'
