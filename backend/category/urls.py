from django.urls import path

from category.views import CategoryProductLV, CategoryLV, CategoryNameProductLV, TopCategoryLV, CategoryDV, \
    CategoryFriendLV

app_name = 'category'

urlpatterns = [
    path('', TopCategoryLV.as_view(), name='list'),
    path('<int:pk>/friend/', CategoryFriendLV.as_view(), name='friend'),
    path('<int:pk>/', CategoryProductLV.as_view(), name='product-list'),
    path('<str:name>/', CategoryNameProductLV.as_view(), name='product-list-name'),
]
