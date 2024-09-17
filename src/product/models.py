from django.db import models

from base.models.helpers.date_time_model import DateTimeModel
from base.models.helpers.named_date_time_model import NamedDateTimeModel
from seller.models import SellerModel

# Create your models here.


class ProductModel(NamedDateTimeModel):
    seller = models.ForeignKey(SellerModel, related_name="seller_ids", on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()
    # quantity = models.PositiveIntegerField()
    # image = models.ImageField()

