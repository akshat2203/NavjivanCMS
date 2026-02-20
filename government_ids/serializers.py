from rest_framework import serializers
from .models import Aadhaar, PAN


class AadhaarSerializer(serializers.ModelSerializer):
    masked = serializers.CharField(read_only=True)

    class Meta:
        model = Aadhaar
        fields = ('id', 'user', 'masked', 'issued_at', 'created_at', 'updated_at')
        read_only_fields = ('masked',)


class PANSerializer(serializers.ModelSerializer):
    masked = serializers.CharField(read_only=True)

    class Meta:
        model = PAN
        fields = ('id', 'user', 'masked', 'created_at')
        read_only_fields = ('masked',)

