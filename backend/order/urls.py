from django.urls import path

from order.views import OrderListView, OrderDetailView, UserOrderListView, OrderProductListView

app_name = 'order'

urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', UserOrderListView.as_view(), name='order-list'),
    path('<str:user_id>/', UserOrderListView.as_view(), name='order-list'),

    path('<int:pk>/product', OrderProductListView.as_view(), name='orderproduct-list'),
    path('<str:user_id>/product', OrderProductListView.as_view(), name='orderproduct-list'),
]
