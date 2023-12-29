from django.urls import path
from apps.gallery.views import PhotoAPIView, VideoAPIView

urlpatterns = [
    path('photo_gallery/', PhotoAPIView.as_view()),
    path('video_gallery/', VideoAPIView.as_view())
]
