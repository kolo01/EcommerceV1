from api.serializers.category_serializer import CategorySerializer
from category.models.category_model import CategoryModel
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()



   