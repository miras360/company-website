from modeltranslation.translator import register, TranslationOptions
from .models import AcademicCouncilInfo, AcademicCouncilDoc, AcademicCouncilMeetings

@register(AcademicCouncilInfo)
class AcademicCouncilInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(AcademicCouncilDoc)
class AcademicCouncilDocTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(AcademicCouncilMeetings)
class AcademicCouncilMeetingsTranslationOptions(TranslationOptions):
    fields = ('title',)