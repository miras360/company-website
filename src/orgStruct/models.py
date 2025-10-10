from django.db import models

# Create your models here.
class OrgStruct(models.Model):
    file = models.FileField(verbose_name='Файл с изображением организационной структуры', upload_to='docs/')
    class Meta:
        verbose_name_plural = "Схемы отделов"
        verbose_name='Схема'
    def __str__(self) -> str:
        return f'Организационная структура'
    
class Departments(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название отдела')
    info = models.TextField(verbose_name='Информация об отделе')
    class Meta:
        verbose_name_plural = "Отделы"
        verbose_name='Отдел'
    def __str__(self) -> str:
        return f'{self.name}'