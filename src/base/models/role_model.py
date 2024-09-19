from base.models.helpers.named_date_time_model import DateTimeModel
from django.db import models


class RoleModel(DateTimeModel):
    name = models.CharField(max_length=255)