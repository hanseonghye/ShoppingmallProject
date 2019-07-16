from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'item'

urlpatterns = [
    path('', ),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', ])
