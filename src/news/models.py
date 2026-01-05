from django.db import models
import os
from django.utils import timezone
from logRegisPages.models import CustomUser

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    title = models.CharField(max_length = 1000, verbose_name='Заголовок')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    content = models.TextField(verbose_name='Контент')
    youtube_url = models.URLField(
        verbose_name='YouTube ссылка',
        blank=True,
        null=True,
        help_text='Ссылка на видео с YouTube (необязательно)'
    ) 
    class Meta:
        verbose_name_plural = "Публикации"
        verbose_name='Публикация'
    def __str__(self) -> str:
        return f'{self.title}: {self.content} ({self.date})'
# Create your models here.

class PostAttachment(models.Model):
    file = models.FileField(upload_to='images/', verbose_name='Файл')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Новость')
    type = models.CharField(max_length = 6, blank=True, null=True, verbose_name='Тип файла' )

    def save(self, *args, **kwargs):
        file_extension = self.file.name.split('.')[-1].lower()
        if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
            self.type = 'img'
        else:
            self.type = 'doc'
        
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = "Файлы"
        verbose_name='Файлы'

    def __str__(self) -> str:
        return f'{self.post}'