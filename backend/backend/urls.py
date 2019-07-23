from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    # swagger
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('redoc'), name='docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='swagger'),

    path('admin/', admin.site.urls, name='admin'),

    path('api/v1/users/', include('user.urls'), name='user'),
    path('api/v1/admin/users/', include('user.admin-urls'), name='admin-user'),

    path('api/v1/categorys/', include('category.urls'), name='category'),
    path('api/v1/admin/categorys/', include('category.admin-urls'), name='admin-category'),

    path('api/v1/products/', include('product.urls'), name='product'),
    path('api/v1/admin/products/', include('product.admin-urls'), name='admin-product'),

    path('api/v1/orders/', include('order.urls'), name='order'),

    path('api/v1/admin/manager/', include('manager.urls'), name='manager'),
]
