from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'username', 'room', 'content')
    search_fields = ('username', 'room', 'content')
    list_filter = ('room', 'username', 'timestamp')
    ordering = ('-timestamp',)
