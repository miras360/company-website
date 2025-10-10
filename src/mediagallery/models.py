from django.db import models
from django.utils import timezone

# Create your models here.
class Mediagallery(models.Model):
    name = models.CharField(max_length=255, verbose_name= "Название фотографии")
    file = models.FileField(verbose_name='Файл', upload_to='mediagallery/')
    date = models.TimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Фотографии"
        verbose_name='Фото'

    def __str__(self) -> str:
        return f'{self.name}'
    