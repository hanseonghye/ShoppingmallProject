from django.db import models

from product.models import ProductDetail
from user.models import CustomUser as User

ORDER_TYPE = (
    ('0', '결제완료'),
    ('1', '상품준비중'),
    ('2', '배송시작'),
    ('3', '배송중'),
    ('4', '배송완료'),
)

PAY_TYPE = (
    ('0', '무통장입금'),
    ('1', '휴대폰소액결제'),
    ('2', '실시간계좌이체'),
    ('3', '신용카드결제'),
    ('4', '카카오페이'),
)


class Order(models.Model):
    user = models.ForeignKey(User, null=True, db_column='user_id', on_delete=models.CASCADE)
    price = models.SmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=ORDER_TYPE)

    username = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    address_detail = models.CharField(max_length=30)
    delivery_message = models.TextField()
    pay_type = models.CharField(max_length=1, choices=PAY_TYPE)

    class Meta:
        db_table = "order_order"

    def __str__(self):
        return f'Order : '


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, null=False, db_column='order_id', on_delete=models.CASCADE)
    product_detail = models.ForeignKey(ProductDetail, null=False, db_column='product_detail_id',
                                       on_delete=models.CASCADE)
    amount = models.SmallIntegerField()
    price = models.SmallIntegerField()

    class Meta:
        db_table = "order_product"

    def __str__(self):
        return f'Order_Product : '
