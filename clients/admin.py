from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ['created_at']
