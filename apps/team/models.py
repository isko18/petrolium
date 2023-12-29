from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.
class Team(TranslatableModel):
    translations = TranslatedFields(
        full_name = models.CharField(
            _('ФИО руководства'),
            max_length=150
        ),
        job_title = models.CharField(
            _("Должность"),
            max_length=150
        )
    )
    image = models.ImageField(
        "Фото руководства",
        upload_to='team/'
    )
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'

class TeamBG(models.Model):
    image = models.ImageField(
        upload_to='bg/',
        verbose_name='Задний фон руководства'
    )
    
    def __str__(self):
        return f'Фото №{self.id}'
    
    class Meta:
        verbose_name = 'Задний фон руководства'
        verbose_name_plural = 'Задний фон руководства'