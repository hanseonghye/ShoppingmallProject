from django.urls import path

from order.views import OrderListView, OrderDetailView, UserOrderListView

app_name = 'order'

urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', UserOrderListView.as_view(), name='order-list'),
    path('<str:user_id>/', UserOrderListView.as_view(), name='order-list'),
]
