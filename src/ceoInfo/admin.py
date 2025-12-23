from django.contrib import admin
from .models import CeoDatas
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.
class CustomCeoInfoAdmin(TranslationAdmin):
    fieldsets = (
        (_('Фотография'), {'fields': ('photo',)}),
        (_('Информация на русском'), {'fields': ('name_ru', 'dateOfBirth_ru', 'post_ru', 'scientific_ru', 'work_ru', 'awards_ru', 'sertificates_ru', 'publications_ru', 'positions_ru', 'education_ru',)}),
        (_('Информация на казахском'), {'fields': ('name_kk', 'dateOfBirth_kk', 'post_kk', 'scientific_kk', 'work_kk', 'awards_kk', 'sertificates_kk', 'publications_kk', 'positions_kk', 'education_kk',)}),
        (_('Информация на английском'), {'fields': ('name_en', 'dateOfBirth_en', 'post_en', 'scientific_en', 'work_en', 'awards_en', 'sertificates_en', 'publications_en', 'positions_en', 'education_en',)}),
    )
    add_fieldsets = (
        (_('Фотография'), {'fields': ('photo',)}),
        (_('Информация на русском'), {'fields': ('name_ru', 'dateOfBirth_ru', 'post_ru', 'scientific_ru', 'work_ru', 'awards_ru', 'sertificates_ru', 'publications_ru', 'positions_ru', 'education_ru',)}),
        (_('Информация на казахском'), {'fields': ('name_kk', 'dateOfBirth_kk', 'post_kk', 'scientific_kk', 'work_kk', 'awards_kk', 'sertificates_kk', 'publications_kk', 'positions_kk', 'education_kk',)}),
        (_('Информация на английском'), {'fields': ('name_en', 'dateOfBirth_en', 'post_en', 'scientific_en', 'work_en', 'awards_en', 'sertificates_en', 'publications_en', 'positions_en', 'education_en',)}),
    )
    list_display = ('name', 'post',)

@admin.register(CeoDatas)
class CeoDatasAdmin(CustomCeoInfoAdmin):
    pass
