from django.urls import path
from rest_framework import routers

from member.cart_views import Cart
from member.member_views import Login, SignUp, MemberInforUpdate, check_id

app_name = 'member'
router = routers.DefaultRouter()

urlpatterns = [
    path('api/member/login/', Login.as_view(), name='login-api'),
    path('api/member/logout/', Login.logout, name='logout-api'),
    path('api/member/signup/', SignUp.as_view(), name='signup-api'),
    path('api/member/accoutinforupdate/', MemberInforUpdate.as_view(), name='memberinforupdate-api'),
    path('api/member/checkid/', check_id, name='checkid-api'),

    path('api/cart/', Cart.as_view(), name='cart-api'),

]
