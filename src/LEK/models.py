from django.db import models
from django.template.defaultfilters import length


class LEK(models.Model):
    title = models.CharField(max_length=255, verbose_name = 'Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    creation_title = models.CharField(max_length=255, verbose_name = 'Название приказа')
    creation = models.FileField(upload_to='LEK/', verbose_name='Приказ о создании', blank=True)
    instructions = models.TextField(verbose_name='Инструкции по обращению', blank=True)
    contacts = models.TextField(verbose_name='Контакты секретариата', blank=True)
    standarts = models.TextField(verbose_name='Стандартные операционные процедуры', blank=True)
    class Meta:
        verbose_name_plural = "Информация"
        verbose_name='Информация'
    def __str__(self) -> str:
        return f'{self.title}'

class LEKRegulation(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название документа')
    document = models.FileField(upload_to='LEK/', verbose_name='Документ', blank=True)
    class Meta:
        verbose_name_plural = "Положения ЛЭК"
        verbose_name='Положение'

    def __str__(self) -> str:
        return f'{self.title}'

class LEKMeetings(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название документа')
    document = models.FileField(upload_to='LEK/', verbose_name='Документ', blank=True)
    class Meta:
        verbose_name_plural = "Заседания ЛЭК"
        verbose_name='Заседание'

    def __str__(self) -> str:
        return f'{self.title}'

class LEKPlans(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название документа')
    document = models.FileField(upload_to='LEK/', verbose_name='Документ', blank=True)
    class Meta:
        verbose_name_plural = "Планы ЛЭК"
        verbose_name='План'

    def __str__(self) -> str:
        return f'{self.title}'
    
class LEKDocForms(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название формы документа')
    link = models.TextField(verbose_name='Ссылка на форму документа')
    class Meta:
        verbose_name_plural = "Формы документов"
        verbose_name='Форма'

    def __str__(self) -> str:
        return f'{self.title}'