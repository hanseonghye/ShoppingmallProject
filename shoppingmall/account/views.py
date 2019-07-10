from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from rest_framework.views import APIView

from account.forms import AccountSignForm


class AccountLogin(APIView):
    id = "user1"
    password = "passw0rd"

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING)
            }
        ),
        responses={
            '200': json.dumps({'result': 'bool', 'data': []})
        },
        operation_id='login',
        operation_description='회원 또는 관리자 로그인 api'
    )
    def post(self, request):
        id = request.POST.get('id', None)
        pw = request.POST.get('password', None)

        if id == self.id and pw == self.password:
            return JsonResponse({
                'result': 'success',
                'data': [1, id]
            })

        return JsonResponse({
            'result': 'fail',
            'data': []
        })


def signup(request):
    if request.method == 'POST':
        form = AccountSignForm(request.POST)

        return HttpResponse("ok")
    else :
        form = AccountSignForm()
        return render(request,'account/sign.html', {'form':form})
