from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.

class Pricing(TranslatableModel):
    translations = TranslatedFields(
        payment = models.CharField(
            _('Форма оплаты'),
            max_length=25,
            blank=True,
            null=True
        ),
        taxes = models.CharField(
            _('Налоги'),
            max_length=25,
            blank=True,
            null=True
        ),
        ai_80 = models.CharField(
            _('Бензин АИ-80'),
            max_length=25,
            blank=True,
            null=True
        ),
        disel = models.CharField(
            _('Дизельное топливо\nмарки Л-0,2-40'),
            max_length=25,
            blank=True,
            null=True
        ),
        mazmut = models.CharField(
            _('Мазмут М-100'),
            max_length=25,
            blank=True,
            null=True
        )
    )
    
    def __str__(self):
        return f'Цены на продукцию {self.id}'
    
    class Meta:
        verbose_name = 'Цена на продукцию'
        verbose_name_plural = 'Цены на продукцию'
    
    
class History(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(
            _('Загаловок'),
            max_length=50,
            blank=True,
            null=True
        ),
        description = models.TextField(
            _('Описание'),
            blank=True,
            null=True
            
        )
        
    )
    date = models.CharField(
            _('Дата'),
            max_length=15
        )
    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'
    
class Jobs(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(
            _('Название вакансии'),
            max_length=50,
            blank=True,
            null=True
        ),
        description = models.CharField(
            _('Описание вакансии'),
            max_length=100,
            blank=True,
            null=True
        )
    )
    requirements = models.FileField(
            _('Требования для вакансии'),
            upload_to='jobs/'
        )
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
    
class Procurement(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(
            _('Название Закупки'),
            max_length=50,
            blank=True,
            null=True
        ),
        description = models.CharField(
            _('Описание Закупки'),
            max_length=100,
            blank=True,
            null=True
        )
    )
    requirements = models.FileField(
            'Требования для Закупки',
            upload_to='jobs/'
        )
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Закупка'
        verbose_name_plural = 'Закупки'

class Banner(models.Model):
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Фотография баннера'
    )

    def __str__(self):
        return f"Фотография {self.id}"
    
    class Meta:
        verbose_name = 'Фотография банера'
        verbose_name_plural = 'Фотографии банера'

class BankDetails(models.Model):
    text = models.TextField(
        'Текст банковских данных'
    )

    def __str__(self):
        return f"Банковские реквизиты {self.id} {self.text[:15]}"
    
    class Meta:
        verbose_name = 'Банковский реквизит'
        verbose_name_plural = 'Банковские реквизиты'