from django.urls import path
from apps.news.views import NewsAPIVIew, MediaAPIVIew,NewsDetailAPIView,NewsDeleteAPIView

urlpatterns = [
    path('', NewsAPIVIew.as_view()),
    path('<int:pk>/', NewsDetailAPIView.as_view()),
    path('delete/<int:pk>/', NewsDeleteAPIView.as_view()),
    path('news_media/', MediaAPIVIew.as_view()),
]
