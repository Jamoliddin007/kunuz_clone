# common/urls.py

from django.urls import path
from common.api_endpoints import MediaFileCreateAPIView
urlpatterns = [
    path('media/upload/', MediaFileCreateAPIView.as_view(), name='media-upload'),
]
