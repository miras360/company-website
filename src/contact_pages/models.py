from django.db import models

# Create your models here.
class Managers(models.Model):
    name = models.CharField(max_length=128, verbose_name='ФИО') 
    post = models.TextField(verbose_name='Должность')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    email = models.CharField(max_length=255, verbose_name='E-mail')
    reception = models.TextField(verbose_name='День и время приема', default = "none")
    show = models.BooleanField(verbose_name='Отображать в 2 таблицах?')

    class Meta:
        verbose_name_plural = "Руководители"
        verbose_name='Руководитель'

    def __str__ (self) -> str:
        return f'{self.name}: {self.post}'
    
class Contacts(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    info = models.TextField(verbose_name='Информация')

    class Meta:
        verbose_name_plural = "Контакты НИИ"
        verbose_name='Контакт'

    def __str__ (self) -> str:
        return f'{self.title}: {self.info}'
    
class InfoAccessFaces(models.Model):
    name = models.CharField(max_length=128, verbose_name='ФИО') 
    post = models.TextField(verbose_name='Должность')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    
    class Meta:
        verbose_name_plural = "Уполномоченые лица по вопросам доступа информации"
        verbose_name='Уполномоченное лицо'

    def __str__ (self) -> str:
        return f'{self.name}: {self.post}'