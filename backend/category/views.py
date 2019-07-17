from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


# class CategoryViewSet(viewsets.ModelViewSet):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()


class CategoryListView(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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
            return Response(serializer.data)

        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(self, request, *args, **kwargs)
