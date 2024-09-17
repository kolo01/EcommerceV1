
from order.models import OrderModel
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        # exclude = ['total_amount']
        fields = "__all__"