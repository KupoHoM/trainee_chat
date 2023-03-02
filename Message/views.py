from rest_framework.generics import CreateAPIView
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from .models import MessageModel
from .serializers import MessageSerializer
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    GenericAPIView,
    ListAPIView, )


class MessagePnation(LimitOffsetPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 5


class MessageViewSet(ModelViewSet):
    queryset = MessageModel.objects.filter()
    pagination_class = MessagePnation
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_read', 'sender', 'thread']



