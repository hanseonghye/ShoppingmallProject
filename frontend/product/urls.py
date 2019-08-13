from django.urls import path

from .views import ProductDV, OrderView

app_name='product'

urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
    path('<pk>/',ProductDV.as_view(), name='detail'),
]