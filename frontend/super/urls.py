from django.urls import path

from .category_views import *
from .views import *
from .product_views import *

app_name='super'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('members/', MemberLV.as_view(), name='member-list'),

    path('products/', ProductLV.as_view(), name='product-list'),
    path('products/add/', ProductCV.as_view(), name='product-add'),
    path('products/update/<pk>', ProductUV.as_view(), name='product-update'),
    path('products/delete/<pk>', ProductDV.as_view(), name='product-delete'),

    path('category//', CategoryLV.as_view(), name='category-list'),
    path('category/add/', CategoryCV.as_view(), name='category-add'),
    path('category/delete/', ProductDV.as_view(), name='category-delete'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]