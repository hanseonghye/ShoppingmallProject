from django.urls import path

from category.views import CategoryListView, CategoryDetailView

app_name = 'category'

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    # path('<int:pk>/', getCategoryProduct, name='category-detail'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('<str:name>/', CategoryDetailView.as_view(), name='category_list_name'),
]
