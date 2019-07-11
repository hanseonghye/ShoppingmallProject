from django.http import HttpResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from member.model import Member
from shoppingmall.jsonResult import JsonResult

name = openapi.Schema(type=openapi.TYPE_STRING)
id = openapi.Schema(type=openapi.TYPE_STRING)
password = openapi.Schema(type=openapi.TYPE_STRING)
email = openapi.Schema(type=openapi.TYPE_STRING)
phone_number = openapi.Schema(type=openapi.TYPE_STRING)
jsonResult = JsonResult("True or False", "success or fail", "{}").toJson()


class Login(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': id,
                'password': password,
            }
        ),
        responses={
            '200': jsonResult
        },
        operation_id='post/api/login',
        operation_description='로그인 요청 api'
    )
    def post(self, request):

        user = Member(request.POST.get('id'), request.POST.get('password'))

        if user.id == 'user1' and user.password == 'passw0rd':
            return HttpResponse(JsonResult(True, "success", {"name": "한성혜", }).toJson(),
                                content_type=u"application/json; charset=utf-8")
        else:
            return HttpResponse(JsonResult(True, "fail", dict()).toJson(),
                                content_type=u"application/json; charset=utf-8")

    @swagger_auto_schema(
        response={
            '200': jsonResult
        },
        operation_id='get/api/login',
        operation_description='로그인 폼 요청 api'
    )
    def get(self, request):
        return HttpResponse(JsonResult(True, "success").toJson(), content_type=u"application/json; charset=utf-8")

    @staticmethod
    @swagger_auto_schema(
        method='GET',
        response={
            '200': jsonResult
        },
        operation_id='get/api/logout',
        operation_description='로그아웃 요청 api'
    )
    @api_view(['GET'])
    def logout(request):
        return HttpResponse(JsonResult(True, True).toJson(),
                            content_type=u"application/json; charset=utf-8")


class SignUp(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': name,
                'id': id,
                'password': password,
                'email': email,
                'phone_number': phone_number
            }
        ),
        responses={
            '200': jsonResult
        },
        operation_id='post/api/signup',
        operation_description='회원가입 요청 api'
    )
    def post(self, request):
        user = Member(request.POST.get('name'), request.POST.get('id'), request.POST.get('password'))

        if user.id == 'user1' and user.password == 'passw0rd':
            return HttpResponse(JsonResult(True, "success", {"name": "한성혜", }).toJson(),
                                content_type=u"application/json; charset=utf-8")
        else:
            return HttpResponse(JsonResult(True, "fail", dict()).toJson(),
                                content_type=u"application/json; charset=utf-8")

    @swagger_auto_schema(
        response={
            '200': jsonResult
        },
        operation_id='get/api/signup',
        operation_description='회원가입 form 요청api'
    )
    def get(self, request):
        return HttpResponse(JsonResult(True, "success").toJson(), content_type=u"application/json; charset=utf-8")


class MemberInforUpdate(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'password1': password,
                'password2': password,
                'email': email,
                'phone_number': phone_number
            }
        ),
        responses={
            '200': jsonResult
        },
        operation_id='post/api/memberinputupdate',
        operation_description='회원정보 변경 요청 api'
    )
    def put(self, request):
        user = Member(request.POST.get('name'), request.POST.get('id'), request.POST.get('password1'))
        return HttpResponse(JsonResult(True, "success", {"name": "한성혜", }).toJson(),
                            content_type=u"application/json; charset=utf-8")

    @swagger_auto_schema(
        response={
            '200': jsonResult
        },
        operation_id='get/api/memberinputupdate',
        operation_description='회원정보 변경 form 요청 api'
    )
    def get(self, request):
        return HttpResponse(JsonResult(True, "success").toJson(), content_type=u"application/json; charset=utf-8")


@swagger_auto_schema(
    method='GET',
    responses={
        '200': jsonResult
    },
    operation_id='get/api/checkid',
    operation_description='회원가입 id 중복값 체크'
)
@api_view(['GET'])
def check_id(request):
    id = request.GET.get('id')
    return HttpResponse(JsonResult(True, Member.check_id(id), dict()).toJson(),
                        content_type=u"application/json; charset=utf-8")

# @swagger_auto_schema(
#     method='GET',
#     response={
#         '200': jsonResult
#     },
#     operation_id='get/api/logout',
#     operation_description='로그아웃 요청 api'
# )
# @api_view(['GET'])
# def logout(request):
#     return HttpResponse(JsonResult(True, True).toJson(),
#                         content_type=u"application/json; charset=utf-8")
