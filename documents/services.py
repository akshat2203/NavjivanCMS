from .models import Document
from django.core.exceptions import ValidationError
import magic


ALLOWED_CONTENT_TYPES = ['application/pdf', 'image/png', 'image/jpeg']
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


class DocumentService:
    @staticmethod
    def validate_and_create(user, uploaded_file, name=None):
        # Validate size
        if uploaded_file.size > MAX_FILE_SIZE:
            raise ValidationError('File too large')

        # Validate content type using python-magic if available or rely on uploaded content_type
        content_type = getattr(uploaded_file, 'content_type', None)
        if content_type is None:
            try:
                content_type = magic.from_buffer(uploaded_file.read(2048), mime=True)
                uploaded_file.seek(0)
            except Exception:
                content_type = 'application/octet-stream'

        if content_type not in ALLOWED_CONTENT_TYPES:
            raise ValidationError('Invalid file type')

        doc = Document.objects.create(user=user, name=name or uploaded_file.name, file=uploaded_file, content_type=content_type, size=uploaded_file.size)
        return doc

