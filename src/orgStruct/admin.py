from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from adminsortable2.admin import SortableAdminMixin

from .models import OrgStruct, Departments

admin.site.register(OrgStruct)

class CustomDepartmentAdmin(SortableAdminMixin, TranslationAdmin):
    sortable_field_name = "sort_order"

    fieldsets = (
        (_('Информация на русском'), {'fields': ('name_ru', 'info_ru')}),
        (_('Информация на казахском'), {'fields': ('name_kk', 'info_kk')}),
        (_('Информация на английском'), {'fields': ('name_en', 'info_en')}),
    )
    add_fieldsets = fieldsets

    list_display = ('name', 'sort_order')   # временно так
    ordering = ('sort_order', 'id',)              # чтобы админка выводила в нужном порядке


@admin.register(Departments)
class DepartmentsAdmin(CustomDepartmentAdmin):
    pass
