from django.db import models
from django.contrib.auth.models import User


class ThreadModel(models.Model):
    participants = models.ManyToManyField(User, verbose_name='threads',)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class MessageModel(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    thread = models.ForeignKey(ThreadModel, on_delete=models.CASCADE,)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
