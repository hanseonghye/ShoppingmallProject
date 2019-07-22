from django.urls import path

from user.views import UserListView, UserDetailView, check_id, check_email, UserAddressDetailView, UserAddressListView

app_name = 'user'

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('<str:user_id>/', UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/address/', UserAddressListView.as_view(), name='user-address'),
    path('<str:user_id>/address/', UserAddressListView.as_view(), name='user-address'),
    # path('<int:pk>/address/<int:address_pk>/', UserAddressDetailView.as_view(), name='user-address'),
    # path('<str:user_id>/address/<int:address_pk>/', UserAddressDetailView.as_view(), name='user-address'),
    path('check/id/<str:user_id>', check_id, name='check-id'),
    path('check/email/<str:email>', check_email, name='check-email'),
]
