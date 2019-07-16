from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from category.views import CategoryViewSet

app_name = 'category'

category_list = CategoryViewSet.as_view({'post': 'create', 'get': 'list'})
category_detail = CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    path('', category_list, name='category-list'),
    path('<int:pk>/', category_detail, name='category-detail'),
    path('<str:name>/', category_detail, name='category-detail-name'),
]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', ])
