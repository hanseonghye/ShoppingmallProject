from django.db import models

from product.models import ProductDetail, Product
from user.models import CustomUser as User

ORDER_TYPE = (
    ('0', '주문전'),
    ('1', '결제전'),
    ('2', '결제완료'),
    ('3', '상품준비중'),
    ('4', '배송시작'),
    ('5', '배송중'),
    ('6', '배송완료'),
)

PAY_TYPE = (
    ('0', '무통장입금'),
    ('1', '휴대폰소액결제'),
    ('2', '실시간계좌이체'),
    ('3', '신용카드결제'),
    ('4', '카카오페이'),
)


class Order(models.Model):
    price = models.SmallIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=ORDER_TYPE)

    user = models.ForeignKey(User, null=True, db_column='user_id', on_delete=models.CASCADE)
    non_user = models.CharField(max_length=30,null=True)
    sender_name = models.CharField(max_length=30)
    sender_email = models.EmailField()
    sender_phone_number = models.CharField(max_length=30)

    receiver_name = models.CharField(max_length=30)
    receiver_phone_number = models.CharField(max_length=30)
    receiver_address = models.CharField(max_length=30)
    delivery_message = models.TextField()
    pay_type = models.CharField(max_length=1, choices=PAY_TYPE)

    class Meta:
        db_table = "order_order"

    def __str__(self):
        return f'Order : {self.id}  {self.user.username}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name='order_products', null=True, blank=True, db_column='order_id',
                              on_delete=models.CASCADE)
    product_detail = models.ForeignKey(ProductDetail, null=True, db_column='product_detail_id',
                                       on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, db_column='product_id', on_delete=models.CASCADE)
    amount = models.SmallIntegerField()
    price = models.SmallIntegerField()
    all_price = models.SmallIntegerField(null=True)

    class Meta:
        db_table = "order_product"

    def __str__(self):
        return f'Order_Product : '
