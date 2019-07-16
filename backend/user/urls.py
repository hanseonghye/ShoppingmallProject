from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserViewSet

app_name = 'user'


user_list = UserViewSet.as_view({'post': 'create', 'get': 'list'})

user_detail = UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    path('', user_list, name='user-list'),
    path('<int:pk>/', user_detail, name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', ])
