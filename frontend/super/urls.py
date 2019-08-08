from django.urls import path

from .views import MemberLV, LoginView, Home, ProductLV, ProductCV

app_name='super'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('members/', MemberLV.as_view(), name='member-list'),
    path('products/', ProductLV.as_view(), name='product-list'),
    path('products/add/', ProductCV.as_view(), name='product-add'),
    path('login/', LoginView.as_view(), name='login'),
]