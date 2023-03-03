from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import ThreadModel
from Message.models import MessageModel
from .serializers import ThreadSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Max


# Create your views here.
class ThreadPnation(LimitOffsetPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 5


class ThreadViewSet(ModelViewSet):
    queryset = ThreadModel.objects.filter()
    pagination_class = ThreadPnation
    serializer_class = ThreadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']


@csrf_exempt
@require_POST
def create_thread(request):
    participants = request.POST.get('participants')

    if participants is None:
        return JsonResponse({'error': 'No participants provided'})

    participants = participants.split(',')

    thread = ThreadModel.objects.filter(participants__id__in=participants).distinct()

    if thread.exists():
        return JsonResponse({'thread_id': thread.first().id})

    thread = ThreadModel.objects.create()
    thread.participants.set(participants)

    return JsonResponse({'thread_id': thread.id})


class ThreadListAPIView(APIView):

    def get(self, request):
        user = request.user
        threads = ThreadModel.objects.filter(participants=user)
        threads_data = []
        for thread in threads:
            last_message = MessageModel.objects.filter(thread=thread).aggregate(Max('created'))['created__max']
            if last_message:
                last_message_obj = MessageModel.objects.filter(thread=thread, created=last_message).first()
                last_message_data = {
                    'sender': last_message_obj.sender.username,
                    'text': last_message_obj.text,
                    'created': last_message_obj.created,
                    'is_read': last_message_obj.is_read,
                }
            else:
                last_message_data = None
            thread_data = {
                'id': thread.id,
                'participants': [participant.username for participant in thread.participants.all()],
                'created': thread.created,
                'updated': thread.updated,
                'last_message': last_message_data,
            }
            threads_data.append(thread_data)
        return Response(threads_data)

