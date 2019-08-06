from django.urls import path

from .views import ProductDV

app_name='product'

urlpatterns = [
    path('<pk>/',ProductDV.as_view(), name='detail')
]