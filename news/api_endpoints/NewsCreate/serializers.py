from rest_framework import serializers
from news.models import News

class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            "title", "slug", "content", "photo", "views_count", 
            "published_at", "category", "region", "author"
        ]
