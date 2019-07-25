from django.urls import path

from order.views import OrderProductListView, OrderManyAddView

app_name = 'order'

urlpatterns = [
    # path('', OrderAddView.as_view(), name='add'),
    path('', OrderManyAddView.as_view(), name='add'),
    path('<int:pk>/', OrderProductListView.as_view(), name='product1'),
    path('<str:user_id>/', OrderProductListView.as_view(), name='product2'),
]
