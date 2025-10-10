from django.db import models

# Create your models here.

class PacientInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    info = models.TextField(verbose_name='Информация')

    class Meta:
        verbose_name_plural = "Правила"
        verbose_name='Правило'

    def __str__ (self) -> str:
        return f'{self.title}: {self.info}'
    
