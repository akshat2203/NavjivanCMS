from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField(read_only=True)
    signature_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'date_of_birth', 'bio', 'photo', 'photo_url', 'signature', 'signature_url')
        read_only_fields = ('photo_url', 'signature_url')

    def get_photo_url(self, obj):
        if obj.photo:
            return obj.photo.url
        return None

    def get_signature_url(self, obj):
        if obj.signature:
            return obj.signature.url
        return None

