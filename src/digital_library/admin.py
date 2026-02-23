from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Book

@admin.register(Book)
class BookAdmin(TranslationAdmin):
    list_display = ('title', 'author', 'description')
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)} # Автозаполнение slug при вводе названия