from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from apps.news.models import News, Media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"
        
class NewsSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=News)
    media = MediaSerializer(many=True, read_only=True)
    class Meta:
        model = News
        fields = "__all__"