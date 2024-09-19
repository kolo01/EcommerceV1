from base.models.person_model import PersonModel
from django.db import models

from base.models.role_model import RoleModel

class SellerModel(PersonModel):
    role = models.ForeignKey(RoleModel,related_name="role_seller_ids", on_delete=models.CASCADE)
    note = models.FloatField()
