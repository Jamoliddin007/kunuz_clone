# common/api_endpoints/MediaFileUpload/serializers.py

from rest_framework import serializers
from common.models import MediaFile


class MediaFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id', 'file']
        read_only_fields = ['id']
