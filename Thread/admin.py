from django.contrib import admin
from .models import ThreadModel
from Message.admin import MessageInline


class ThreadAdm(admin.ModelAdmin):
    inlines = (MessageInline,)
    list_display = ("id", "created", "updated")
    list_filter = ("id", "created", "updated")
    list_per_page = 10
    list_per_show_all = 100


admin.site.register(ThreadModel, ThreadAdm)
