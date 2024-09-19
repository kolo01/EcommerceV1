from base.models.helpers.named_date_time_model import NamedDateTimeModel
from django.db import models
from base.models.role_model import RoleModel


class PersonModel(NamedDateTimeModel):
    last_name = models.CharField(max_length=255)        
    gender = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    birthday = models.DateField()
    contact_number = models.CharField(max_length=255)
    



    class Meta:
        abstract = True