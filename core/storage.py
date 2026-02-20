from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from django.core.files.storage import FileSystemStorage

# Storage adapter to switch between local filesystem (dev) and S3 (prod) via settings.DEFAULT_FILE_STORAGE

class UserMediaStorage:
    """Factory for user-media storage backends. Use in models or services.

    Use settings.DEFAULT_FILE_STORAGE to control which backend is active.
    """

    @staticmethod
    def get_storage():
        if settings.DEFAULT_FILE_STORAGE.endswith("S3Boto3Storage") or 's3' in settings.DEFAULT_FILE_STORAGE.lower():
            return S3Boto3Storage()
        return FileSystemStorage(location=settings.MEDIA_ROOT)


class UserS3Storage(S3Boto3Storage):
    """S3 storage configured to store files under a dedicated prefix for the project."""

    bucket_name = settings.AWS_S3_BUCKET_NAME
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False


class LocalMediaStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        super().__init__(location=settings.MEDIA_ROOT)

