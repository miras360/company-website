from django.db import models

class LOKGeneralInfo(models.Model):
    # Главный экран
    hero_title = models.CharField(max_length=255, verbose_name="Заголовок комплекса (напр. LOK Astana)")
    hero_bg = models.ImageField(upload_to='lok_media/', blank=True, null=True, verbose_name="Фон главного экрана")
    
    # Ценность
    value_title = models.CharField(max_length=255, verbose_name="Заголовок: Ценность", default="Ценность проекта")
    value_text = models.TextField(verbose_name="Текст: Ценность")
    
    # Особенности
    features_title = models.CharField(max_length=255, verbose_name="Заголовок: Особенности", default="Особенности")
    features_text = models.TextField(verbose_name="Текст: Особенности")
    
    # Контакты
    contacts_title = models.CharField(max_length=255, verbose_name="Заголовок контактов", default="Наши контакты")
    contacts_text = models.TextField(verbose_name="Текст контактов (адрес, телефон)")

    class Meta:
        verbose_name = "Главная страница ЛОК"
        verbose_name_plural = "Главная страница ЛОК"

    def __str__(self):
        return "Настройки страницы ЛОК"

class LOKRoom(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название номера (напр. Люкс)")
    short_desc = models.TextField(verbose_name="Краткое описание (для карточки)")
    full_desc = models.TextField(verbose_name="Полное описание (для окна)")
    cover_image = models.ImageField(upload_to='lok_rooms/', verbose_name="Главное фото")
    sort_order = models.PositiveIntegerField(default=0, verbose_name="Порядок вывода")

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номерной фонд"
        ordering = ['sort_order']

    def __str__(self):
        return self.name

class LOKRoomGallery(models.Model):
    room = models.ForeignKey(LOKRoom, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='lok_rooms/gallery/', verbose_name="Фото")

class LOKService(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Краткое описание", blank=True)
    image = models.ImageField(upload_to='lok_services/', verbose_name="Иллюстрация")
    sort_order = models.PositiveIntegerField(default=0, verbose_name="Порядок вывода")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['sort_order']

    def __str__(self):
        return self.name