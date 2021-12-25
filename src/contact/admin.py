from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    """ Message Model for admin """
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email',)
    readonly_fields = ('created_at',)


admin.site.register(Message, MessageAdmin)
