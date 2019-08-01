from django.urls import path, re_path

from order.views import OrderManyCV, UserOrderRV, UserOrderLV, UserOrderNameLV

app_name = 'order'

urlpatterns = [
    path('', OrderManyCV.as_view(), name='add'),
    path('user/<int:pk>/', UserOrderLV.as_view(), name='list'),
    path('user/<str:user_id>/', UserOrderNameLV.as_view(), name='name-list'),
    path('user/<int:pk>/<int:orderpk>', UserOrderRV.as_view(), name='detail'),
    path('user/<str:user_id>/<int:orderpk>', UserOrderRV.as_view()),
]
