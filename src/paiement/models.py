from django.db import models

from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.

class PaiementModel(DateTimeModel):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name