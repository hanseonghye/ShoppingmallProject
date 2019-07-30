from django.conf import settings
from django.urls import path
import oauth2_provider.views as oauth2_views

app_name = 'oauth2_provider'

urlpatterns = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name='authorize'),
    path('token/', oauth2_views.TokenView.as_view(), name='token'),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name='revoke-token'),
]

if settings.DEBUG:
    urlpatterns += [
        path('applications/', oauth2_views.ApplicationList.as_view(), name='list'),
        path('applications/register/', oauth2_views.ApplicationRegistration.as_view(), name='register'),
        path('applications/<int:pk>/', oauth2_views.ApplicationDetail.as_view(), name='detail'),
        path('applications/<int:pk>/delete/', oauth2_views.ApplicationDelete.as_view(), name='delete'),
        path('applications/<int:pk>/update/', oauth2_views.ApplicationUpdate.as_view(), name='update'),
    ]

    urlpatterns += [
        path('authorized-token/', oauth2_views.AuthorizedTokensListView.as_view(), name='authorized-token-list'),
        path('authorized-token/<int:pk>/delete/', oauth2_views.AuthorizedTokenDeleteView.as_view(),
             name='authorized-token-delete'),
    ]
