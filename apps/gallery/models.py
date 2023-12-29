from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields
from moviepy.editor import VideoFileClip
# Create your models here.
class Photo(models.Model):
    image = models.ImageField(
        _('Фото'),
        upload_to='gallery/'
    )
    def __str__(self):
        return f"Фото номер: {self.pk}"
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
        
class Video(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(
            _('Загаловок'),
            max_length=100,
        )
    )
    video = models.FileField(
        _('Видео'),
        upload_to='gallery/'
    )
    screen_image = models.ImageField(
        _('Фото заставки'),
        upload_to='screen_image/'    
    )
    duration = models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return f"Видео номер: {self.pk}"
    
    def save(self, *args, **kwargs):
        if not self.duration or self.duration == '':
            try:
                clip = VideoFileClip(self.video.path)
                self.duration = clip.duration
                print(clip.duration)
            except Exception as e:
                self.duration = '2Мин'
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'