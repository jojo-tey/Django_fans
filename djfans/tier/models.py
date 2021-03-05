from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Tier(models.Model):
    number = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(max_length=800, verbose_name='Description')
