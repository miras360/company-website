from django.db import models

# Create your models here.
class WorkersInfo(models.Model):
    name = models.CharField(max_length=128, verbose_name='ФИО') 
    post = models.TextField(verbose_name='Должность')
    work_exp = models.CharField(max_length=255, verbose_name = 'Стаж')
    sertificates = models.TextField(verbose_name = 'Сертификат специалиста')

    class Meta:
        verbose_name_plural = "Сотрудники"
        verbose_name='Сотрудник'

    def __str__ (self) -> str:
        return f'{self.name}: {self.post}'
    