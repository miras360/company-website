from django.db import models

class index_page(models.Model):
    mission = models.TextField(verbose_name='Миссия')
    view = models.TextField(verbose_name='Видение')
    class Meta:
        verbose_name_plural = "Информации"
        verbose_name='Информация'
    def __str__(self) -> str:
        return f'{self.mission}'
    
class openInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    file = models.FileField(verbose_name='Документ', upload_to='docs/')
    class Meta:
        verbose_name_plural = "Приказ о прозрачности"
        verbose_name='Документ'
    def __str__(self) -> str:
        return f'{self.title}: {self.file}'