from rest_framework import serializers

from users.models.customer_model import CustomerModel


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = '__all__'