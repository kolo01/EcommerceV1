from api.serializers.seller_serializer import SellerSerializer
from rest_framework import viewsets
from users.models.seller_model import SellerModel



class SellerViewset(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    queryset = SellerModel.objects.all()