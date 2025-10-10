from django.db import models

# Create your models here.
class MedServices(models.Model):
    file = models.FileField(verbose_name='Файл медицинских услуг', upload_to='docs/')

    class Meta:
        verbose_name_plural = "Документы"
        verbose_name='Документ'

    def __str__(self) -> str:
        return f'Медицинские услуги'
    
class Medicine(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Основной текст')
    class Meta:
        verbose_name_plural = "Медицина"
        verbose_name='Информация о медицине'
    def __str__(self) -> str:
        return f'{self.title}'