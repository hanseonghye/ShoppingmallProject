from django.urls import path

from user.views import UserListView, UserDetailView, check_id, check_email

app_name = 'user'

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('check/id/<str:user_id>', check_id, name='check-id'),
    path('check/email/<str:email>', check_email, name='check-email'),
]
