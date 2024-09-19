from django.db import models

from base.models.helpers.date_time_model import DateTimeModel
from base.models.helpers.named_date_time_model import NamedDateTimeModel
from category.models.category_model import CategoryModel
from users.models.seller_model import SellerModel


# Create your models here.


class ProductModel(NamedDateTimeModel):
    seller = models.ForeignKey(SellerModel, related_name="seller_ids", on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, related_name="category_ids", on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    # quantity = models.PositiveIntegerField()
    image = models.URLField()

