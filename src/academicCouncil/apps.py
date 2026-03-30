from django.apps import AppConfig

class AcademiccouncilConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'academicCouncil'  # Вот эта критическая строка
    verbose_name = "Ученый совет"