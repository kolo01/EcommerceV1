from rest_framework import serializers
from users.models.seller_model import SellerModel



class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerModel
        fields = '__all__'