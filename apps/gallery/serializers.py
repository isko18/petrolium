from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from apps.gallery.models import Photo, Video

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class VideoSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Video)
    class Meta:
        model = Video
        fields = '__all__'