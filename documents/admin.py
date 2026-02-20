from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'content_type', 'size', 'created_at')
    search_fields = ('name', 'user__email')

