from django.db import models
from apps.utils.models import Timestamps


# this is like a migration
class WaitlistEntry(Timestamps, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.TextField(max_length=100)
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='email_address'
    )
    notes = models.TextField()

    # When you want to change how the model will appear
    # on the admin side
    # A verbose is an alternative name
    class Meta:
        verbose_name_plural = 'Waitlist entries'
