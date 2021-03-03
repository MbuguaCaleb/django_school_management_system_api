from django.db import models
from apps.utils.models import Timestamps
# Create your models here.


class Certificate(Timestamps, models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default="", blank=True)

