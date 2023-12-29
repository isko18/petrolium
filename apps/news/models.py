from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.
class News(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(
            _('Загаловок'),
            max_length=100,
        ),
        description = models.TextField(_('Описание'))
    )
    main_image = models.ImageField(
        'Главное фото',
        upload_to='news/'
    )
    created = models.CharField(
        'Дата',
        max_length=15
    )
    
    def __str__(self):
        return f"Новость-{self.created}"
    
    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')
        
class Media(models.Model):
    image = models.ImageField(
        'Доп фото для новости',
        upload_to='news/'
    )
    news = models.ForeignKey(
        News,
        related_name='media',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"Фото новости: {self.news.title}"
    class Meta:
        verbose_name = 'Фото новости'
        verbose_name_plural = 'Фото новости'
