from django.db import models
from django.utils import timezone


class Apple(models.Model):
    name = models.CharField('名前', max_length=20)
    seed = models.CharField('種子親', max_length=20)
    pollen = models.CharField('花粉親', max_length=20)

    created_at = models.DateTimeField(default=timezone.now)

    __yamdl__ = True
