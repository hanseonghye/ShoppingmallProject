import requests
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView
from django.conf import settings
from .provider import CustomProvider


class CustomAdapter(OAuth2Adapter):
    provider_id = CustomProvider.id

    access_token_url = '{}/oauth2/token/'.format(settings.OAUTH_SERVER_BASEURL)
    authorize_url = '{}/oauth2/authorize/'.format(settings.OAUTH_SERVER_BASEURL)
    # profile_url = '{}/api/v1/users/login/'.format(settings.OAUTH_SERVER_BASEURL)


    # def complete_login(self, request, app, access_token, **kwargs):
    #     headers = {'Authorization': 'Bearer {0}'.format(access_token.token)}
    #     print(headers)
    #     resp = requests.get(self.profile_url, headers=headers)
    #     extra_data = resp.json()
    #     print(extra_data)
    #     return self.get_provider().sociallogin_from_response(request, extra_data)


oauth2_login = OAuth2LoginView.adapter_view(CustomAdapter)
oauth2_callback = OAuth2CallbackView.adapter_view(CustomAdapter)