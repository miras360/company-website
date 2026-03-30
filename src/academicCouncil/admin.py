from django.contrib import admin
from .models import AcademicCouncilInfo, AcademicCouncilDoc, AcademicCouncilMeetings
from modeltranslation.admin import TranslationAdmin

@admin.register(AcademicCouncilInfo)
class AcademicCouncilInfoAdmin(TranslationAdmin):
    list_display = ('title', 'description')

@admin.register(AcademicCouncilDoc)
class AcademicCouncilDocAdmin(TranslationAdmin):
    list_display = ('title', 'document')

@admin.register(AcademicCouncilMeetings)
class AcademicCouncilMeetingsAdmin(TranslationAdmin):
    list_display = ('title', 'document')