from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(People)
class PeopleAdmin(TranslationAdmin):
    list_display = ( 'post',)

@admin.register(Doctors)
class DoctorsAdmin(TranslationAdmin):
    list_display = ( 'title', 'photo', 'content')

@admin.register(Teachers)
class TeachersAdmin(TranslationAdmin):
    list_display = ( 'title', 'photo', 'content')