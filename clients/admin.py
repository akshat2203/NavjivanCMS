from django.contrib import admin
from .models import ClientProfile, ClientDocument, ClientQualification

# Register your models here.
admin.site.register(ClientProfile)
admin.site.register(ClientDocument)
admin.site.register(ClientQualification)
