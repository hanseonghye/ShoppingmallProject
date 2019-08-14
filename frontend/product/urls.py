from django.urls import path

from .views import ProductDV, OrderView, OrderDV

app_name='product'

urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
    path('order/<pk>', OrderDV.as_view(), name='order_detail'),
    path('<pk>/',ProductDV.as_view(), name='detail'),
]