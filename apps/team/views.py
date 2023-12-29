from rest_framework import generics
from apps.team.models import Team, TeamBG
from apps.team.serializers import TeamSerializer, TeamBGSerializer

class TeamAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDeleteAPIView(generics.DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamBGAPIView(generics.ListAPIView):
    queryset = TeamBG.objects.all()
    serializer_class = TeamBGSerializer