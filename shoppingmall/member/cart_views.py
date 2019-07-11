from django.http import HttpResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from shoppingmall.jsonResult import JsonResult

id = openapi.Schema(type=openapi.TYPE_STRING)
product_no = openapi.Schema(type=openapi.TYPE_INTEGER)
product_detail_no = openapi.Schema(type=openapi.TYPE_INTEGER)
amount = openapi.Schema(type=openapi.TYPE_INTEGER)
jsonResult = JsonResult("True or False", "success or fail", "{}").toJson()


class Cart(APIView):

    @swagger_auto_schema(
        response={
            '200': jsonResult
        },
        operation_id='get/api/item/cartlist',
        operation_description='장바구니확인 요청 api'
    )
    def get(self, request, id=None):
        return HttpResponse(JsonResult(True, "success").toJson(), content_type=u"application/json; charset=utf-8")

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'produt_no': product_no,
                'product_detail_no': product_detail_no,
                'amount': amount
            }
        ),
        response={
            '200': jsonResult
        },
        operation_id='get/api/item/cartlist',
        operation_description='장바구니 추가 요청 api'
    )
    def post(self, request, id):
        return HttpResponse(JsonResult(True, "success").toJson(), content_type=u"application/json; charset=utf-8")

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'produt_no': product_no,
                'product_detail_no': product_detail_no,
                'amount': amount
            }
        ),
        response={
            '200': jsonResult
        },
        operation_id='get/api/item/cartlist',
        operation_description='장바구니 수정 요청 api'
    )
    def put(self, request, id):
        return HttpResponse(JsonResult(True, "success").toJson(), content_type=u"application/json; charset=utf-8")

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'produt_no': product_no,
                'product_detail_no': product_detail_no,
            }
        ),
        response={
            '200': jsonResult
        },
        operation_id='get/api/item/cartlist',
        operation_description='장바구니 삭제 요청 api'
    )
    def delete(self, request, id):
        return HttpResponse(JsonResult(True, "success").toJson(), content_type=u"application/json; charset=utf-8")

