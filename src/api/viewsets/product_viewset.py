from api.serializers.product_serializer import ProductSerializer
from product.models import ProductModel
from rest_framework import viewsets


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()