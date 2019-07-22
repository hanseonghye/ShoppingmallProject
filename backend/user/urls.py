from django.urls import path

from user.views import UserListView, UserDetailView, check_id, check_email

app_name = 'user'

urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('<str:user_id>/', UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/address/', UserAddressDetailView.as_view(), name='user-detail'),
    path('<str:user_id>/address/', UserAddressDetailView.as_view(), name='user-detail'),
    path('check/id/<str:user_id>', check_id, name='check-id'),
    path('check/email/<str:email>', check_email, name='check-email'),
]
