from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Document
        fields = ('id', 'name', 'file_url', 'content_type', 'size', 'created_at')

    def get_file_url(self, obj):
        return obj.file.url if obj.file else None

