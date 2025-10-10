from django.db import models

# Create your models here.
class CeoDatas(models.Model):
    name = models.CharField(max_length=255, verbose_name = 'Имя руководителя')
    dateOfBirth = models.CharField(max_length=255, verbose_name = 'Дата рождания')
    post = models.CharField(max_length=255, verbose_name='Должность', blank=True)
    scientific = models.TextField(verbose_name = 'Научная степень', blank=True)
    work = models.TextField(verbose_name = 'Трудовая деятельность', blank=True)
    positions = models.TextField(verbose_name = 'Должности', blank=True)
    awards = models.TextField(verbose_name = 'Награды', blank=True)
    sertificates = models.TextField(verbose_name = 'Сертификаты', blank=True)
    publications = models.TextField(verbose_name = 'Публикации', blank=True)
    photo = models.FileField(verbose_name= 'Фото руководителя', upload_to='images/')
    education = models.TextField(verbose_name = 'Образование')

    class Meta:
        verbose_name_plural = "Информация о руководителе"
        verbose_name='Руководитель'

    def __str__ (self) -> str:
        return f'{self.name}'
    

    
