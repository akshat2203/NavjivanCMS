from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'actor', 'subject', 'action')
    search_fields = ('actor__email', 'subject__email', 'action')
    readonly_fields = ('actor', 'subject', 'action', 'message', 'created_at')

