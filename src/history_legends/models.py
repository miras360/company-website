from django.db import models

# Create your models here.
class History(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    poem = models.TextField(verbose_name='Стихотворение')
    info = models.TextField(verbose_name='Информация')

    class Meta:
        verbose_name_plural = "История НИИ"
        verbose_name='История НИИ'

    def __str__ (self) -> str:
        return f'{self.title}'