from rest_framework import serializers
from .models import ThreadModel
from simple_chat.settings import THREAD_SETTINGS
from rest_framework.validators import ValidationError

participants_count = THREAD_SETTINGS.get("number_of_participants", 2)


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadModel
        fields = "__all__"

    def validate_participants(self, value):
        if len(value) > participants_count:
            raise ValidationError({"detail": "Too many participants"})
