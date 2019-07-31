from django.urls import path

from user.views import UserLV

app_name = 'admin-user'

urlpatterns = [
    path('', UserLV.as_view(), name='list'),
]
