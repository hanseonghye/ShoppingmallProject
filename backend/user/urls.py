from django.urls import path
from .views import *

app_name = 'user'


urlpatterns = [
    path('', UserCV.as_view(), name='register'),
    path('<int:pk>/', UserDV.as_view(), name='detail'),
    path('<str:user_id>/', UserNameDV.as_view(), name='name-detail'),
    path('<int:pk>/address/', UserAddressLV.as_view(), name='address-list'),
    path('<str:user_id>/address/', UserAddressNameLV.as_view(), name='address-name-list'),
    path('check/id/<str:user_id>', check_id, name='check-id'),
    path('check/email/<str:email>', check_email, name='check-email'),
]
