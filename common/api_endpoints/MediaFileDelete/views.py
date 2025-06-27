from rest_framework.generics import DestroyAPIView
from rest_framework import permissions
from common.models import MediaFile


class MediaFileDestroyAPIView(DestroyAPIView):
    """
    Delete a media file by ID
    """
    queryset = MediaFile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"
