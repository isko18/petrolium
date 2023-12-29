from django.urls import path
from apps.team.views import TeamAPIView,TeamDeleteAPIView, TeamBGAPIView

urlpatterns = [
    path('', TeamAPIView.as_view()),
    path('<int:pk>/', TeamDeleteAPIView.as_view()),
    path('team_images/', TeamBGAPIView.as_view()),
]
