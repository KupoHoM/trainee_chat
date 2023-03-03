from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import MessageModel
from .serializers import MessageSerializer


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


@api_view(['GET'])
def unread_messages_count(request, user_id):
    count = MessageModel.objects.filter(thread__participants=user_id, is_read=False).count()
    return Response({'unread_messages_count': count})


class MarkMessageAsRead(APIView):
    def put(self, request, message_id):
        message = get_object_or_404(MessageModel, id=message_id)
        message.is_read = True
        message.save()
        return Response(status=status.HTTP_200_OK)


class MarkMessagesAsRead(APIView):
    def put(self, request):
        message_ids = request.data.get('message_ids', [])
        if not message_ids:
            return Response({'message_ids': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        messages = MessageModel.objects.filter(Q(id__in=message_ids) & Q(is_read=False))
        if not messages:
            return Response({'message_ids': 'No unread messages found.'}, status=status.HTTP_404_NOT_FOUND)
        messages.update(is_read=True)
        return Response(status=status.HTTP_200_OK)
