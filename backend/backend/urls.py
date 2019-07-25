from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
import oauth2_provider.views as oauth2_views

from backend.views import test

oauth2_urlpatterns = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name='authorize'),
    path('token/', oauth2_views.TokenView.as_view(), name='token'),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name='revoke-token'),
]

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

if settings.DEBUG:
    oauth2_urlpatterns += [
        path('applications/', oauth2_views.ApplicationList.as_view(), name='list'),
        path('applications/register/', oauth2_views.ApplicationRegistration.as_view(), name='register'),
        path('applications/<int:pk>/', oauth2_views.ApplicationDetail.as_view(), name='detail'),
        path('applications/<int:pk>/delete/', oauth2_views.ApplicationDelete.as_view(), name='delete'),
        path('applications/<int:pk>/update/', oauth2_views.ApplicationUpdate.as_view(), name='update'),
    ]

    oauth2_urlpatterns += [
        path('authorized-token/', oauth2_views.AuthorizedTokensListView.as_view(), name='authorized-token-list'),
        path('authorized-token/<int:pk>/delete/', oauth2_views.AuthorizedTokenDeleteView.as_view(),
             name='authorized-token-delete'),
    ]

urlpatterns = [
    # swagger
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('redoc'), name='docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='swagger'),
    path('oauth2/', include('user.auth'), name='oauth2_provider'),

    path('admin/', admin.site.urls, name='admin'),

    path('api/v1/users/', include('user.urls'), name='user'),
    path('api/v1/admin/users/', include('user.admin-urls'), name='admin-user'),

    path('api/v1/categorys/', include('category.urls'), name='category'),
    path('api/v1/admin/categorys/', include('category.admin-urls'), name='admin-category'),

    path('api/v1/products/', include('product.urls'), name='product'),
    path('api/v1/admin/products/', include('product.admin-urls'), name='admin-product'),

    path('api/v1/orders/', include('order.urls'), name='order'),
    path('api/v1/admin/orders/', include('order.admin-urls'), name='admin-order'),

    path('api/v1/carts/', include('cart.urls'), name='cart'),

    path('api/v1/admin/manager/', include('manager.urls'), name='manager'),
    # path('api/hello/',test.as_view())
]