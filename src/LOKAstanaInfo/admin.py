from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from adminsortable2.admin import SortableAdminMixin
from .models import LOKGeneralInfo, LOKRoom, LOKRoomGallery, LOKService

@admin.register(LOKGeneralInfo)
class LOKGeneralInfoAdmin(TranslationAdmin):
    def has_add_permission(self, request):
        # Защита от дурака: лендинг может быть только один
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

# Встроенная галерея для номерного фонда
class LOKRoomGalleryInline(admin.TabularInline):
    model = LOKRoomGallery
    extra = 1

@admin.register(LOKRoom)
class LOKRoomAdmin(SortableAdminMixin, TranslationAdmin):
    inlines = [LOKRoomGalleryInline]
    list_display = ('name', 'sort_order')
    ordering = ('sort_order', 'id')

@admin.register(LOKService)
class LOKServiceAdmin(SortableAdminMixin, TranslationAdmin):
    list_display = ('name', 'sort_order')
    ordering = ('sort_order', 'id')