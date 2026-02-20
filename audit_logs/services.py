from .models import AuditLog


class AuditService:
    @staticmethod
    def log(actor, subject, action, message=''):
        AuditLog.objects.create(actor=actor, subject=subject, action=action, message=message)

