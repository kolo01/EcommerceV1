from api.serializers.cart_serializer import CartSerializer
from cart.models import CartModel
from rest_framework import viewsets


class CartViewset(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = CartModel.objects.all()