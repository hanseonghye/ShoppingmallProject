from django.urls import path

from .views import ManagerUserListView, ManagerUserDetailView

app_name = 'manager'

urlpatterns = [
    path('', ManagerUserListView.as_view(), name='amdin-list'),
    path('<int:pk>', ManagerUserDetailView.as_view(), name='admin-detail'),
]
