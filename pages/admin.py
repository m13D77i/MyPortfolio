from django.contrib import admin

from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'subject', 'created_at',]
    ordering = ('-created_at',)
    search_fields = ('fullname', 'email',)