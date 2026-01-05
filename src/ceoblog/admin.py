from django.contrib import admin
from .models import PostCeo
from .models import PostAttachment
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.

class PostAttachmentInline(admin.TabularInline):
    model = PostAttachment
    extra = 1
    fields = ('file',)   # type можно убрать, если не хочешь видеть
    verbose_name = _('Файл')
    verbose_name_plural = _('Файлы (фото/документы)')

class CustomPostCeoAdmin(TranslationAdmin):
    fieldsets = (
        (_('Автор поста'), {'fields': ('author',)}),
        (_('Информация на русском'), {'fields': ('title_ru', 'content_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'content_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'content_en',)}),
        (_('Медиа'), {
            'fields': ('youtube_url',),
            'description': _('Ссылка на YouTube-видео')}),
        (_('Дополнительная информация'), {'fields': ('date',)}),
    )
    add_fieldsets = (
        (_('Автор поста'), {'fields': ('author',)}),
        (_('Информация на русском'), {'fields': ('title_ru', 'content_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'content_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'content_en',)}),
        (_('Медиа'), {'fields': ('youtube_url',)}),
    )
    list_display = ('title', 'content', 'youtube_url', 'date')

@admin.register(PostCeo)
class PostAdmin(CustomPostCeoAdmin):
    inlines = [PostAttachmentInline]