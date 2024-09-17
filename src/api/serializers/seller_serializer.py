from rest_framework import serializers
from seller.models import SellerModel


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerModel
        fields = '__all__'