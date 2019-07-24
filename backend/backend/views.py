from django.http import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework import generics

from myModule import myMixins as mixins


class test(ProtectedResourceView, mixins.RetrieveModelMixin,
           mixins.UpdateModelMixin,
           mixins.DestroyModelMixin,
           mixins.ListModelMixin,
           generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello@")
