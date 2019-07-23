from django.urls import path

from product.views import *

app_name = 'admin-product'

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductModifyDetailView.as_view(), name='product-detail'),
    path('<int:pk>/options/', OptionListView.as_view(), name='productoption-list'),
    path('<int:pk>/options/<int:optionpk>/', OptionValueListView.as_view(), name='productoption-detail'),

    # path('<int:pk>/options/', OptionListView.as_view(), name='productoption-list'),
    # path('<int:pk>/options/<int:id>', OptionDetailView.as_view(), name='productoption-detail'),

    # path('options/', OptionListView.as_view(), name='option-list'),
    # path('options/<int:pk>/', OptionDetailView.as_view(), name='option-detail'),

    # path('optiondetails/', OptionDetailListlView.as_view(), name='optiondetail-list'),
    # path('optiondetails/<int:pk>/', OptionDetailDetailView.as_view(), name='optiondetail-detail'),

    # path('productdetails/', ProductDetailListView.as_view(), name='productdetail-list'),
    # path('productdetails/<int:pk>/', ProductDetailDetailView.as_view(), name='productdetail-detail'),
]
