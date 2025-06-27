from django.urls import path
from .api_endpoints.NewsCreate import NewsCreateAPIView

urlpatterns = [
    path('create/', NewsCreateAPIView.as_view(), name='news-create'),
]
