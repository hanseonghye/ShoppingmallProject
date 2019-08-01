from django.db import models

from category.models import Category


class Product(models.Model):
    name = models.CharField('Name', max_length=30, null=False)
    price = models.SmallIntegerField('Price')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id')

    is_stock = models.BooleanField('Stock')
    is_display = models.BooleanField('Display')
    is_option = models.BooleanField('Option')

    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify_Date', auto_now=True)

    file_url = models.TextField()
    image_url = models.TextField()

    class Meta:
        db_table = "product_product"

    def __str__(self):
        return f'Product : {self.name}'


class ProductDetail(models.Model):
    # id = models.CharField(primary_key=True, max_length=255)
    # name = models.CharField('Name', max_length=30)
    price = models.SmallIntegerField('Price')
    stock = models.SmallIntegerField('Stock')

    option_no = models.IntegerField('Option_No')
    option_name = models.CharField('Option_Name', max_length=30)

    product = models.ForeignKey(Product,related_name='product_details', db_column='product_id', null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "product_product_detail"

    def __str__(self):
        return f'ProductDetail : {self.option_name}, {self.product.name}'


class Option(models.Model):
    name = models.CharField(max_length=30, null=False)
    product = models.ForeignKey(Product, related_name='product_options', null=False, on_delete=models.CASCADE, db_column='product_id')

    class Meta:
        db_table = "product_option"

    def __str__(self):
        return f'Option : {self.name}, {self.product}'


class OptionDetail(models.Model):
    name = models.CharField(max_length=30, null=False)
    option = models.ForeignKey(Option, null=False, related_name='option_details', on_delete=models.CASCADE, db_column='option_id')

    class Meta:
        db_table = "product_option_detail"

    def __str__(self):
        return f'OptionDetail : {self.name}, {self.option.name} , {self.option.procudt.name}'
