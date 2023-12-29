from rest_framework import generics
from apps.news.models import News, Media
from apps.news.serializers import NewsSerializer, MediaSerializer

class NewsAPIVIew(generics.ListAPIView):
    queryset = News.objects.all()[::-1]
    serializer_class = NewsSerializer

class NewsDeleteAPIView(generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class MediaAPIVIew(generics.ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer