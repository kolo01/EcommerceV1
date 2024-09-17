from django.db import models

from base.models.helpers.date_time_model import DateTimeModel
from product.models import ProductModel

# Create your models here.

class CartModel(DateTimeModel):
    product = models.ManyToManyField(ProductModel, related_name='product_ids')

    

    def __str__(self):
        return f"Cart N° {self.id}"