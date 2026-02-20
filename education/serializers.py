from rest_framework import serializers
from .models import Education


class EducationSerializer(serializers.ModelSerializer):
    marksheet_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Education
        fields = ('id', 'user', 'level', 'board', 'passing_year', 'percentage', 'marksheet', 'marksheet_url', 'created_at')
        read_only_fields = ('marksheet_url', 'created_at')

    def get_marksheet_url(self, obj):
        if obj.marksheet:
            return obj.marksheet.url
        return None

