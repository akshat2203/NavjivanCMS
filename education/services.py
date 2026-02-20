from .models import Education
from django.core.exceptions import PermissionDenied


class EducationService:
    @staticmethod
    def create_education_for_user(user, data):
        # Business validation: passing_year range, percentage bounds, file type check delegated elsewhere
        data['user'] = user
        edu = Education.objects.create(**data)
        return edu

    @staticmethod
    def get_user_educations(user):
        # Prefetch optimizations can be added when joining with other data
        return Education.objects.filter(user=user).order_by('-passing_year')

