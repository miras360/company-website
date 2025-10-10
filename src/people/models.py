from django.db import models

# Create your models here.

class People(models.Model):
    name=models.CharField(max_length=128, verbose_name='ФИО')
    post = models.CharField(max_length=128, verbose_name='Должность')
    image = models.ImageField(upload_to='people/', verbose_name='Фото')
    director = models.BooleanField(verbose_name='Руководитель')
    doctor=models.BooleanField(verbose_name='Врач')
    teacher=models.BooleanField(verbose_name='Педагог')

    class Meta:
        verbose_name_plural = "Персонал"
        verbose_name='Человек'
    def __str__(self) -> str:
        return f'{self.name}'
    
class Doctors(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Основной текст')
    class Meta:
        verbose_name_plural = "Информация о врачах"
        verbose_name='Информация о врачах'
    def __str__(self) -> str:
        return f'{self.title}'

class Teachers(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Основной текст')
    class Meta:
        verbose_name_plural = "Информация о педагогах"
        verbose_name='Информация о педагогах'
    def __str__(self) -> str:
        return f'{self.title}'