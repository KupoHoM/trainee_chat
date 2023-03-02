from django.db import models
from django.contrib.auth.models import User


class ThreadModel(models.Model):
    participants = models.ManyToManyField(User, verbose_name='threads',)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
