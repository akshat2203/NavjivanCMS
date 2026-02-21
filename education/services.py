from .models import Education
from audit_logs.services import AuditService


class EducationService:
    @staticmethod
    def create_education(user, data, actor=None):
        education = Education.objects.create(user=user, **data)
        AuditService.log(actor or user, user, 'education.create', f'Created education record level={education.level}')
        return education

    @staticmethod
    def update_education(education, data, actor=None):
        for field, value in data.items():
            setattr(education, field, value)
        education.save()
        AuditService.log(actor or education.user, education.user, 'education.update', f'Updated education record id={education.id}')
        return education

    @staticmethod
    def delete_education(education, actor=None):
        user = education.user
        edu_id = education.id
        level = education.level
        education.delete()
        AuditService.log(actor or user, user, 'education.delete', f'Deleted education record id={edu_id} level={level}')
