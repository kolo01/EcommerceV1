from paiement.models import PaiementModel
from rest_framework import serializers


class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaiementModel
        fields = '__all__'