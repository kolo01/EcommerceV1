
from django.http import HttpResponse
from api.serializers.order_serializer import OrderSerializer
from order.models import OrderModel
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()

   