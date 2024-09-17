from django.db import models

from base.models.helpers.date_time_model import DateTimeModel
from cart.models import CartModel
from paiement.models import PaiementModel

# Create your models here.


class OrderModel(DateTimeModel):
    cart = models.OneToOneField(CartModel,related_name="cart_ids",on_delete=models.CASCADE)
    payment = models.OneToOneField(PaiementModel,related_name="payment_ids",on_delete=models.SET_NULL, null=True)
    total_amount = models.FloatField()
    