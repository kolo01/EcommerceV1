from api.serializers.product_serializer import ProductSerializer
from product.models import ProductModel
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from users.models.seller_model import SellerModel
class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()



    def create ( self, request):
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        seller_id = data["seller"]
        if serializer.is_valid():
            seller = SellerModel.objects.filter(id=seller_id)
            if  seller:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
             
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)