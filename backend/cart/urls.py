from django.urls import path

from .views import CartListView, CartDetailView

app_name = 'cart'

urlpatterns = [
    path('<int:pk>', CartListView.as_view(), name='list'),
    path('<int:pk>/<int:cartpk>', CartDetailView.as_view(), name='detail'),
]
