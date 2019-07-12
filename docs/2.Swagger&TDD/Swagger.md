# Swagger

장고에서 문서화에 많이 사용되는 Swagger openAPI 라이브러리인 `drf_yasg`를 사용했다.

### 간단한 사용법

1. 설치

   `# pip install drf-yasg`

2. 설정

   `settings.py`파일의 installed_apps에 등록한다.

   ```python
   INSTALLED_APPS = [
       ...
       'drf_yasg',
   ]
   ```

    `urls.py`파일에서 타고들어갈 url도 설정해준다.

   ```python
   schema_view = get_schema_view(
       openapi.Info(
           title="Snippets API",
           default_version='v1',
           description="Test description",
           terms_of_service="https://www.google.com/policies/terms/",
           contact=openapi.Contact(email="contact@snippets.local"),
           license=openapi.License(name="BSD License"),
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
   )
   
   urlpatterns = [
       # swagger
       url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
       path('docs/', schema_view.with_ui('redoc'), name='docs'),
       path('swagger/', schema_view.with_ui('swagger'), name='swagger'),
   	...
   ]
   ```

   

3. CBV 에서 사용하기

   ```python
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
           operation_id='로그인',
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
           operation_id='로그인 폼',
           operation_description='로그인 폼 요청 api'
       )
       def get(self, request):
           return HttpResponse(JsonResult(True, "success").toJson(), content_type=u"application/json; charset=utf-8")
   
   ```

   해당 View에 `APIView`를 상속하고 다음과 같이 문서화 해준다.

   메소드가 get이면 get method에 해당한다.

   `urls.py`에서 해당 view만 등록해 주면 method에 따라서 알아서 해당 메서드에 들어간다.

4. FBV에서 사용하기

   ```python
   @swagger_auto_schema(
       method='GET',
       responses={
           '200': jsonResult
       },
       operation_id='회원가입 id 중복값 체크',
       operation_description='회원가입 id 중복값 체크 api'
   )
   @api_view(['GET'])
   def check_id(request):
       return HttpResponse(
           JsonResult(True, "success" if Member.check_id(request.GET.get('id', None)) else "fail").toJson(),
           content_type=u"application/json; charset=utf-8")
   ```

   FBV의 경우 method를 명시해 줘야하는것 같다.


해당 앞에서 swagger에 들어가기 위한 url로 들어가면 이렇게 보여준다.

![swagger ui]()



   