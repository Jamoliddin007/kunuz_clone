# common/urls.py

from django.urls import path
from common.api_endpoints import MediaFileCreateAPIView, MediaFileDestroyAPIView
urlpatterns = [
    path('media/upload/', MediaFileCreateAPIView.as_view(), name='media-upload'),
    path("media/delete/<int:id>/", MediaFileDestroyAPIView.as_view(), name="media-delete"),

]
