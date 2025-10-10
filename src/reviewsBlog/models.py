from django.db import models
from django.utils import timezone

class Reviews(models.Model):
    author = models.CharField(max_length=255, verbose_name = "ФИО")
    IIN = models.CharField(max_length=255, verbose_name = 'ИИН')
    review = models.TextField(verbose_name='Отзыв')
    date = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        verbose_name_plural = "Отзывы"
        verbose_name='Отзыв'

    def __str__(self) -> str:
        return f'{self.author}: {self.IIN} ({self.date})'
    
class Answer(models.Model):
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    answer = models.TextField(verbose_name='Ответ на отзыв')
    date = models.DateTimeField(auto_now=timezone.now)
    class Meta:
        verbose_name_plural = "Ответы на отзывы"
        verbose_name='Ответ на отзыв'
    def __str__(self) -> str:
        return f'{self.review.author}: {self.answer} ({self.date})'