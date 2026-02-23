from django.db import models
from django.urls import reverse
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    author = models.CharField(max_length=255, verbose_name="Автор")
    slug = models.SlugField(unique=True, verbose_name="URL-адрес (slug)")
    description = models.TextField(blank=True, verbose_name="Описание")
    cover = models.ImageField(upload_to='media/books/covers/', verbose_name="Обложка", blank=True, null=True)
    file = models.FileField(upload_to='media/books/files/', verbose_name="Книга (файл)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Поле для полнотекстового поиска
    search_vector = SearchVectorField(null=True, editable=False)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        indexes = [
            # Индекс для быстрого поиска по названию и автору
            GinIndex(fields=['search_vector']), 
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('digital_library:book_detail', kwargs={'slug': self.slug})