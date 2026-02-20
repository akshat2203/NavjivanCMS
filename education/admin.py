from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'passing_year', 'percentage')
    search_fields = ('user__email', 'board')

