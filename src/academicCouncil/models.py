from django.db import models

class AcademicCouncilInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    
    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = "Информация"

    def __str__(self):
        return f'{self.title}'

class AcademicCouncilDoc(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название документа')
    document = models.FileField(upload_to='academicCouncil/', verbose_name='Документ', blank=True)
    
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = "Документы (Скачивание)"

    def __str__(self):
        return f'{self.title}'

class AcademicCouncilMeetings(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название документа')
    document = models.FileField(upload_to='academicCouncil/', verbose_name='Документ', blank=True)
    
    class Meta:
        verbose_name = 'Заседание'
        verbose_name_plural = "Заседания (Просмотр)"

    def __str__(self):
        return f'{self.title}'