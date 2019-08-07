from django.urls import path

from .views import MemberLV, LoginView

app_name='super'

urlpatterns = [
    path('members/', MemberLV.as_view(), name='member-list'),
    path('login/', LoginView.as_view(), name='login'),
]