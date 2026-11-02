from django.db import models

from apps.base.models import OrderedModel, SoftDeleteModel


class CategoryModel(OrderedModel, SoftDeleteModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['name',],
    #             condition=models.Q(deleted_at__isnull=True),
    #             name='unique_category_name',
    #         )
    #     ]
