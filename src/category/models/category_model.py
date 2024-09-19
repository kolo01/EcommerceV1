from base.models.helpers.date_time_model import DateTimeModel
from django.db import models

# Create your models here.
class CategoryModel(DateTimeModel):
    name= models.CharField(max_length=225)