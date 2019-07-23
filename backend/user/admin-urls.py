from django.urls import path

from user.views import UserListView

app_name = 'admin-user'

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
]
