from django.contrib import admin
from .models import ChatMessage

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'source_ip']
    list_filter = ['text', 'source_ip']
    search_fields = ['text', 'source_ip']


admin.site.register(ChatMessage, ChatMessageAdmin)

