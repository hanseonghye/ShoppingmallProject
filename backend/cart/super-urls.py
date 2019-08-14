from django.urls import path

urlpatterns=[
    path('', CartLV.as_view(),'list'),
]