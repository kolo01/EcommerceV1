
from api.serializers.paiement_serializer import PaiementSerializer
from paiement.models import PaiementModel
from rest_framework import viewsets


class PaiementViewset(viewsets.ModelViewSet):
    serializer_class = PaiementSerializer
    queryset = PaiementModel.objects.all()