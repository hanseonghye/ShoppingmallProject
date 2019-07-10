from django.urls import path
from rest_framework import routers

from account.views import AccountLogin, signup

app_name = 'account'
router = routers.DefaultRouter()

urlpatterns = [
    path('login/', AccountLogin.as_view(), name='login'),
    path('signup/', signup, name='signup')
]
