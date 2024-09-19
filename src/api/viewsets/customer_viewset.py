
from rest_framework import viewsets

from api.serializers.customer_serializer import CustomerSerializer
from users.models.customer_model import CustomerModel



class CustomerViewset(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = CustomerModel.objects.all()