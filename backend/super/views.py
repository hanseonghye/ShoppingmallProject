from django.contrib import auth
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def login(request):
    user = auth.authenticate( user_id=request.POST['user_id'], password= request.POST['password'],is_admin=True)
    if not user:
        return Response({"result":"fail", "message":"아이디또는 패스워드를 다시 확인해 주세요.", "data":None}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"result":"success", "message":None, "data":user.username}, status=status.HTTP_200_OK)