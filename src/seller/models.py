from django.db import models

from base.models.helpers.named_date_time_model import NamedDateTimeModel

# Create your models here.


class SellerModel(NamedDateTimeModel):
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    birthday = models.DateField()
    contact_number = models.CharField(max_length=255)