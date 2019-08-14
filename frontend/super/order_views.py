import requests
from django.views.generic import ListView, TemplateView

from frontend import default

root_url= default.root_url
api_url = default.api_url
header = default.headers

class OrderLV(TemplateView):
    template_name = 'super/order-list.html'

    def get_context_data(self, **kwargs):
        response = requests.get(root_url+api_url+"super/orders/")
        data = dict()

        if response.status_code is not 200:
            data['orders'] = []
            return data
        data['orders'] = response.json()['data']
        return data


class OrderDV(TemplateView):
    template_name = "super/order-detail.html"

    def get_context_data(self, **kwargs):
        response = requests.get(root_url+api_url+"super/orders/"+kwargs['pk'])
        if response.status_code is not 200 :
            pass
        data=response.json()['data']
        return data
