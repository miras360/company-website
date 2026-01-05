from django.contrib import admin
from .models import Post, PostAttachment
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.
class CustomPostAdmin(TranslationAdmin):
    fieldsets = (
        (_('Автор'), {'fields': ( 'author',)}),
        (_('Информация на русском'), {'fields': ( 'title_ru', 'content_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'content_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'content_en',)}),
        (_('Медиа'), {
            'fields': ('youtube_url',),
            'description': _('Ссылка на YouTube-видео')}),
        (_('Дополнительная информация'), {'fields': ( 'date', )}),
    )
    add_fieldsets = (
        (_('Автор'), {'fields': ( 'author',)}),
        (_('Информация на русском'), {'fields': ( 'title_ru', 'content_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'content_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'content_en',)}),
        (_('Медиа'), {
            'fields': ('youtube_url',)}),
        (_('Дополнительная информация'), {'fields': ( 'date', )}),
    )
    list_display = ( 'title', 'content',)

@admin.register(Post)
class PostAdmin(CustomPostAdmin):
    pass

class CustomPostAttAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Новость'), {'fields': ('post',)}),
        (_('Файл'), {'fields': ('file', 'type',)}),
    )
    add_fieldsets = (
        (_('Новость'), {'fields': ('post',)}),
        (_('Файл'), {'fields': ('file', 'type',)}),
    )
    list_display = ('post',)

    class Meta:
        verbose_name_plural = "Файлы"
        verbose_name = 'Файлы'

@admin.register(PostAttachment)
class PostAttAdmin(CustomPostAttAdmin):
    pass