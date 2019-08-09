from django.urls import path

from .views import *

app_name = 'super-product'

urlpatterns = [
    path('', SuperProductLV.as_view(), name='list'),
    path('add/', ProductCV.as_view(), name='add'),
    path('<int:pk>/', ProductDV.as_view(), name='detail'),

    path('<int:pk>/options/', OptionLV.as_view(), name='option-list'),
    path('<int:pk>/options/<int:optionpk>/', OptionDV.as_view(), name='option-detail'),

    path('<int:pk>/options/<int:optionpk>/detail/', OptionDetailLV.as_view(), name='optiondetail-list'),
    path('<int:pk>/options/<int:optionpk>/detail/<int:detailpk>/', OptionDetailDV.as_view(),
         name='optiondetail-detail'),

]
