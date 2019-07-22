from django.urls import path

from category.views import CategoryProductView

app_name = 'category'

urlpatterns = [
    path('<int:pk>/', CategoryProductView.as_view(), name='category-detail'),
    path('<str:name>/', CategoryProductView.as_view(), name='category_list_name'),
]
