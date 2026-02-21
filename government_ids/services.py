from .models import Aadhaar, PAN
from core.encryption import encrypt_field, decrypt_field
from audit_logs.services import AuditService
from django.core.exceptions import PermissionDenied


class GovernmentIDService:
    @staticmethod
    def set_aadhaar(user, aadhaar_number: str, issued_at=None, actor=None):
        # Validate format & compute last4
        last4 = aadhaar_number[-4:]
        blob = encrypt_field(aadhaar_number)
        aadhaar, _ = Aadhaar.objects.update_or_create(user=user, defaults={'encrypted': blob, 'last4': last4, 'issued_at': issued_at})
        AuditService.log(actor or user, user, 'aadhaar.update', f'Updated Aadhaar last4={last4}')
        return aadhaar

    @staticmethod
    def set_pan(user, pan_number: str, actor=None):
        last4 = pan_number[-4:]
        blob = encrypt_field(pan_number)
        pan, _ = PAN.objects.update_or_create(user=user, defaults={'encrypted': blob, 'last4': last4})
        AuditService.log(actor or user, user, 'pan.update', f'Updated PAN last4={last4}')
        return pan

    @staticmethod
    def get_masked_aadhaar(user):
        aadhaar = Aadhaar.objects.filter(user=user).first()
        if not aadhaar:
            return None
        return aadhaar.masked()

    @staticmethod
    def get_masked_pan(user):
        pan = PAN.objects.filter(user=user).first()
        if not pan:
            return None
        return pan.masked()

    @staticmethod
    def delete_aadhaar(user, actor=None):
        aadhaar = Aadhaar.objects.filter(user=user).first()
        if aadhaar:
            last4 = aadhaar.last4
            aadhaar.delete()
            AuditService.log(actor or user, user, 'aadhaar.delete', f'Deleted Aadhaar last4={last4}')
            return True
        return False

    @staticmethod
    def delete_pan(user, actor=None):
        pan = PAN.objects.filter(user=user).first()
        if pan:
            last4 = pan.last4
            pan.delete()
            AuditService.log(actor or user, user, 'pan.delete', f'Deleted PAN last4={last4}')
            return True
        return False

