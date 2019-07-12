from django.forms import model_to_dict
from django.http import HttpResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from member.test_model import Cart
from shoppingmall.jsonResult import JsonResult

id = openapi.Schema(type=openapi.TYPE_STRING)
product_no = openapi.Schema(type=openapi.TYPE_INTEGER)
product_detail_no = openapi.Schema(type=openapi.TYPE_INTEGER)
amount = openapi.Schema(type=openapi.TYPE_INTEGER)
jsonResult = JsonResult("True or False", "success or fail", "{}").toJson()


class Carts(APIView):

    @swagger_auto_schema(
        response={
            '200': jsonResult
        },
        operation_id='장바구니 확인',
        operation_description='장바구니확인 요청 api'
    )
    def get(self, request):
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
        operation_id='장바구니 추가',
        operation_description='장바구니 추가 요청 api'
    )
    def post(self, request):
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
        operation_id='장바구니 수정',
        operation_description='amount가 0보다 크면 성공'
    )
    def put(self, request):
        amount = request.data.get('amount', 0)

        if amount > 0:

            cart_item = Cart(1, request.data.get('product_no', None), request.data.get('product_detail_no', None),
                             amount)
            print(dict(cart_item))
            return HttpResponse(JsonResult(True, "success", dict(cart_item)).toJson(),
                                content_type=u"application/json; charset=utf-8")
        return HttpResponse(JsonResult(True, "fail").toJson(), content_type=u"application/json; charset=utf-8")

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
        operation_id='장바구니 삭제',
        operation_description='장바구니 삭제 요청 api'
    )
    def delete(self, request, id):
        return HttpResponse(JsonResult(True, "success").toJson(), content_type=u"application/json; charset=utf-8")
