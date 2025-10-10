from django.utils import timezone
from django.db import models

# Create your models here.
class Ads(models.Model):
    title = models.CharField(max_length=255, verbose_name = 'Заголовок объявления')
    
    class Meta:
        verbose_name_plural = "Группа объявлений"

    def __str__(self) -> str:
        return f'{self.title}'
    
class Files(models.Model):
    ads=models.ForeignKey(Ads, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name = 'Название файла')
    file = models.FileField(verbose_name='Файл', upload_to='docs/')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    type = models.CharField(max_length = 6, blank=True, null=True )

    def save(self, *args, **kwargs):
        file_extension = self.file.name.split('.')[-1].lower()
        print(file_extension)
        self.type = file_extension
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = "файлы и объявления"
        verbose_name='файл или объявление'
    def __str__(self) -> str:
        return f'{self.name}: ({self.date})'