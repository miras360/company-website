from django.db import models

# Create your models here.
class Ethica(models.Model):
    name = models.CharField(max_length=255, verbose_name = 'Название файла')
    file = models.FileField(verbose_name='Файл', upload_to='docs/')
    type = models.CharField(max_length = 6, blank=True, null=True )

    def save(self, *args, **kwargs):
        file_extension = self.file.name.split('.')[-1].lower()
        print(file_extension)
        self.type = file_extension
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = "Документы об этике"
        verbose_name='Документ'

    def __str__(self) -> str:
        return f'{self.name}'