from modeltranslation.translator import register, TranslationOptions
from .models import Departments, OrgStruct

@register(Departments)
class PostTranslationoptions(TranslationOptions):
    fields = ('name', 'info', 'head_name')

@register(OrgStruct)
class OrgStructTranslationOptions(TranslationOptions):
    fields = ('file',)