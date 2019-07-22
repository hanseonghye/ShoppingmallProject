from django.urls import path

from order.views import OrderListView, OrderDetailView

app_name = 'order'

urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
