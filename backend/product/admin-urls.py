from django.urls import path

from .views import *

app_name = 'admin-product'

urlpatterns = [
    path('', ProductCV.as_view(), name='add'),
    path('<int:pk>/', ProductDV.as_view(), name='detail'),
    path('<int:pk>/options/', OptionLV.as_view(), name='option-list'),
    path('<int:pk>/options/<int:optionpk>/', OptionDV.as_view(), name='option-detail'),

    # path('<int:pk>/options/', OptionListView.as_view(), name='productoption-list'),
    # path('<int:pk>/options/<int:id>', OptionDetailView.as_view(), name='productoption-detail'),

    # path('options/', OptionListView.as_view(), name='option-list'),
    # path('options/<int:pk>/', OptionDetailView.as_view(), name='option-detail'),

    # path('optiondetails/', OptionDetailListlView.as_view(), name='optiondetail-list'),
    # path('optiondetails/<int:pk>/', OptionDetailDetailView.as_view(), name='optiondetail-detail'),

    # path('productdetails/', ProductDetailListView.as_view(), name='productdetail-list'),
    # path('productdetails/<int:pk>/', ProductDetailDetailView.as_view(), name='productdetail-detail'),
]
