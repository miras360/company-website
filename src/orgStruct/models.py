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
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Порядок")

    name = models.CharField(max_length=255, verbose_name='Название отдела')
    info = models.TextField(verbose_name='Информация об отделе')

    class Meta:
        verbose_name_plural = "Отделы"
        verbose_name = 'Отдел'
        ordering = ["sort_order", "id"]

    def __str__(self) -> str:
        return f'{self.name}'