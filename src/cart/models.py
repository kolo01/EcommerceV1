from django.db import models

from base.models.helpers.date_time_model import DateTimeModel
from paiement.models import PaiementModel
from product.models import ProductModel
from users.models.customer_model import CustomerModel

# Create your models here.

class CartModel(DateTimeModel):
    product = models.ManyToManyField(ProductModel, related_name='product_ids')
    user = models.ForeignKey(CustomerModel, related_name='customer_ids', on_delete=models.CASCADE)
    total_amount = models.FloatField(default=0)

    

    def __str__(self):
        return f"Cart N° {self.id} from {self.user.name}"