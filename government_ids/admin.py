from django.contrib import admin
from .models import Aadhaar, PAN


@admin.register(Aadhaar)
class AadhaarAdmin(admin.ModelAdmin):
    list_display = ('user', 'last4', 'issued_at', 'created_at')
    search_fields = ('user__email', 'last4')


@admin.register(PAN)
class PANAdmin(admin.ModelAdmin):
    list_display = ('user', 'last4', 'created_at')
    search_fields = ('user__email', 'last4')

