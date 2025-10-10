from django.db import models

# Create your models here.

    
class Booking(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Основной текст')
    class Meta:
        verbose_name_plural = "Бронирование"
        verbose_name='Информация о Бронировании'
    def __str__(self) -> str:
        return f'{self.title}'