"""simple_chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from Message.views import MessageViewSet, unread_messages_count, MarkMessageAsRead, MarkMessagesAsRead
from Thread.views import create_thread, ThreadViewSet, ThreadListAPIView


router = routers.DefaultRouter()
router.register(r'message', MessageViewSet, basename='message')
router.register(r'thread', ThreadViewSet, basename='thread')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api/message/<int:user_id>/unread_messages_count/', unread_messages_count, name='unread_messages_count'),
    path('api/messages/<int:message_id>/read/', MarkMessageAsRead.as_view()),
    path('api/messages/read/', MarkMessagesAsRead.as_view()),

    path('create_thread/', create_thread, name='create_thread'),
    path('threads/', ThreadListAPIView.as_view(), name='thread-list-api'),



    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
