from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from adminsortable2.admin import SortableAdminMixin
from .models import OrgStruct, Departments

@admin.register(OrgStruct)
class OrgStructAdmin(TranslationAdmin):
    pass

@admin.register(Departments)
class DepartmentsAdmin(SortableAdminMixin, TranslationAdmin):
    pass