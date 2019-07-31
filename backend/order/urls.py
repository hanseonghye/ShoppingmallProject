from django.urls import path, re_path

from order.views import OrderManyCV, UserOrderRV, UserOrderLV, UserOrderNameLV

app_name = 'order'

urlpatterns = [
    path('', OrderManyCV.as_view(), name='add'),
    path('<int:pk>/', UserOrderLV.as_view(), name='list'),
    path('<str:user_id>/', UserOrderNameLV.as_view(), name='name-list'),
    path('<int:pk>/<int:orderpk>', UserOrderRV.as_view(), name='detail'),
    path('<str:user_id>/<int:orderpk>', UserOrderRV.as_view()),
]
