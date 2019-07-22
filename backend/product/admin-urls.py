from django.urls import path

from product.views import ProductListView, ProductDetailView, OptionListView, OptionDetailView, OptionDetailDetailView, \
    OptionDetailListlView, ProductOptionListView, ProductDetailDetailView, ProductDetailListView

app_name = 'admin-product'

urlpatterns = [
    path('<int:pk>/options/', ProductOptionListView.as_view(), name='productoption-list'),

    path('options/', OptionListView.as_view(), name='option-list'),
    path('options/<int:pk>/', OptionDetailView.as_view(), name='option-detail'),

    path('optiondetails/', OptionDetailListlView.as_view(), name='optiondetail-list'),
    path('optiondetails/<int:pk>/', OptionDetailDetailView.as_view(), name='optiondetail-detail'),


    path('productdetails/', ProductDetailListView.as_view(), name='productdetail-list'),
    path('productdetails/<int:pk>/', ProductDetailDetailView.as_view(), name='productdetail-detail'),
]
