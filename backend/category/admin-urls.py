from django.urls import path

from category.views import CategoryLV, CategoryDV

app_name = 'admin-category'

urlpatterns = [
    path('', CategoryLV.as_view(), name='list'),
    path('<int:pk>/', CategoryDV.as_view(), name='detail'),
    path('<str:name>/', CategoryDV.as_view(), name='detail-name'),
]