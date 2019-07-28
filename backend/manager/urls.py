from django.urls import path

from .views import ManagerUserLV, ManagerUserDV

app_name = 'manager'

urlpatterns = [
    path('', ManagerUserLV.as_view(), name='list'),
    path('<int:pk>', ManagerUserDV.as_view(), name='detail'),
]
