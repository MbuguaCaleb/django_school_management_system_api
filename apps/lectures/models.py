from django.db import models
from apps.utils.models import Timestamps


# this is like a migration
class Lecture(Timestamps, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lecturer_name = models.CharField(max_length=100, default='', blank=True)
    date = models.DateField()
    slides_url = models.CharField(max_length=255)
