from django.db import models
from django.contrib.auth.models import User
from Thread.models import ThreadModel


class MessageModel(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True, verbose_name='Text message')
    thread = models.ForeignKey(ThreadModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.text
