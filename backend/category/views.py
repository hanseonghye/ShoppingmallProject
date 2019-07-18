from rest_framework import generics
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer
from myModule import myMixins as mixins


class CategoryListView(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})

    def post(self, request, *args, **kwargs):
        data = self.create(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})


class CategoryDetailView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        if 'name' in self.kwargs:
            queryset = Category.objects.filter(name=kwargs['name'])
            serializer = self.get_serializer(queryset, many=True)
            return Response({"result": "success", "message": None, "data": serializer.data})

        data = self.retrieve(self, request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})

    def put(self, request, *args, **kwargs):
        try:
            data = self.update(request, *args, **kwargs)
        except Exception as e:
            return Response({"result": "fail", "message": None, "data": None})
        return Response({"result": "success", "message": None, "data": data})

    def delete(self, request, *args, **kwargs):
        data = self.delete(request, *args, **kwargs)
        return Response({"result": "success", "message": None, "data": data})
