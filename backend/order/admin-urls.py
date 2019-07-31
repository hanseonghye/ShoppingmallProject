from django.urls import path

from order.views import OrderLV, UserOrderUV

app_name = 'admin-order'
urlpatterns = [
    path('', OrderLV.as_view(), name='list'),
    path('<int:pk>', UserOrderUV.as_view(), name='update'),
]
