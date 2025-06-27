from rest_framework.generics import CreateAPIView
from .serializers import NewsCreateSerializer
from news.models import News

class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
