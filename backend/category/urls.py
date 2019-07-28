from django.urls import path

from category.views import CategoryProductLV, CategoryLV

app_name = 'category'

urlpatterns = [
    path('', CategoryLV.as_view(), name='list'),
    path('<int:pk>/', CategoryProductLV.as_view(), name='product-list'),
    path('<str:name>/', CategoryProductLV.as_view(), name='product-list-name'),
]
