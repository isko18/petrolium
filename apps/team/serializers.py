from rest_framework import serializers
from apps.team.models import Team, TeamBG
from parler_rest.fields import TranslatedFieldsField

class TeamSerializer(serializers.ModelSerializer):
    translations = TranslatedFieldsField(shared_model=Team)
    class Meta:
        model = Team
        fields = '__all__'

class TeamBGSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamBG
        fields = '__all__'
