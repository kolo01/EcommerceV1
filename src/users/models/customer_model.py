from base.models.person_model import PersonModel
from django.db import models

from base.models.role_model import RoleModel


class CustomerModel(PersonModel):
    role = models.ForeignKey(RoleModel,related_name="role_customer_ids", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)