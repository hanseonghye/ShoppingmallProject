from django.urls import path

from category.views import CategoryLV, CategoryDV, CategoryNameDV

app_name = 'super-category'

urlpatterns = [
    path('', CategoryLV.as_view(), name='list'),
    path('name/<str:name>', CategoryNameDV.as_view(), name='name-detail'),
    path('<int:pk>/', CategoryDV.as_view(), name='detail'),
    path('<str:name>/', CategoryDV.as_view(), name='detail-name'),
]