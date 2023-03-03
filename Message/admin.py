from django.contrib import admin
from .models import MessageModel


class MessageAdm(admin.ModelAdmin):
    list_display = ('sender', 'text', 'thread', 'created', 'is_read')
    search_fields = ('sender',)
    list_per_page = 10
    list_per_show_all = 100
    fields = ('text',)


class MessageInline(admin.TabularInline):
    model = MessageModel
    extra = 0


admin.site.register(MessageModel, MessageAdm)
