from cart.models import CartModel
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = '__all__'