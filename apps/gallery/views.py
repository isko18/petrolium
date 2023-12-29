from rest_framework import generics
from apps.gallery.models import Photo, Video
from apps.gallery.serializers import PhotoSerializer, VideoSerializer

class PhotoAPIView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    
class VideoAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer