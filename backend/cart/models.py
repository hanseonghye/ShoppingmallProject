from django.db import models
from product.models import ProductDetail, Product
from user.models import CustomUser as User


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, db_column='user_id', on_delete=models.CASCADE)
    non_user = models.CharField(max_length=30,null=True)
    product = models.ForeignKey(Product, null=False, db_column='product_id', on_delete=models.CASCADE)
    product_detail = models.ForeignKey(ProductDetail, null=True, db_column='product_detail_id',
                                       on_delete=models.CASCADE)

    amount = models.SmallIntegerField()
    expiry_date = models.DateTimeField()

    class Meta:
        db_table = "cart_cart"

    def __str__(self):
        return f'Cart : {self.user}, {self.non_user} '
