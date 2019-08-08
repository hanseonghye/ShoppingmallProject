from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
import oauth2_provider.views as oauth2_views

from backend import oauth
from backend.views import test

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
    path('oauth2/', include('backend.oauth'), name='oauth2_provider'),
    # path('api/v1/rest-auth/', include('rest_auth.urls')),

    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('api/v1/users/', include('user.urls'), name='user'),
    path('api/v1/super/users/', include('user.super-urls'), name='super-user'),

    path('api/v1/categorys/', include('category.urls'), name='category'),
    path('api/v1/super/categorys/', include('category.super-urls'), name='super-category'),

    path('api/v1/products/', include('product.urls'), name='product'),
    path('api/v1/super/products/', include('product.super-urls'), name='super-product'),

    path('api/v1/orders/', include('order.urls'), name='order'),
    path('api/v1/super/orders/', include('order.super-urls'), name='super-order'),

    path('api/v1/carts/', include('cart.urls'), name='cart'),

    path('api/v1/super/', include('super.urls'), name='super'),
    # path('api/hello/',test.as_view())
]
