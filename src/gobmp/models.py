from django.db import models

# Create your models here.
class GOBMP(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    info = models.TextField(verbose_name='Информация')
    adult = models.TextField(verbose_name='Взрослые', blank=True)
    children = models.TextField(verbose_name='Дети', blank=True)
    additinaly = models.TextField(verbose_name='Для получения путевки необходимо')
    class Meta:
        verbose_name_plural = "ГОБМП"
        verbose_name='Информация о ГОБМП'

    def __str__ (self) -> str:
        return f'{self.title}'