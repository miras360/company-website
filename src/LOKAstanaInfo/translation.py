from modeltranslation.translator import register, TranslationOptions
from .models import LOKGeneralInfo, LOKRoom, LOKService

@register(LOKGeneralInfo)
class LOKGeneralInfoTranslationOptions(TranslationOptions):
    fields = ('hero_title', 'value_title', 'value_text', 'features_title', 'features_text', 'contacts_title', 'contacts_text')

@register(LOKRoom)
class LOKRoomTranslationOptions(TranslationOptions):
    fields = ('name', 'short_desc', 'full_desc')

@register(LOKService)
class LOKServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')