from django.urls import path

from order.views import OrderListView, OrderDetailView

app_name = 'admin-order'
urlpatterns = [
    path('', OrderListView.as_view(), name='list'),
    path('<int:pk>', OrderDetailView.as_view(), name='detail'),
]
