from django.db import models
from django.core.validators import ValidationError

# Create your models here.

# Блок "О нашей компании"

class ShortInfoAboutCompany(models.Model):
    # Информация о компании

    text_about = models.TextField('Описание')

    def __str__(self):
        return "Описание"

    class Meta:

        verbose_name = 'Краткая информация о компании'
        verbose_name_plural = 'Краткая информация о компании'

class InfoItem(models.Model):
    # Пункты списка достоинств

    info_name = models.CharField('Достоинство', 
                                max_length=20,  
                                unique=True
                                )
    info_description = models.TextField('Описание')

    def __str__(self):
        return "Пункт: " + self.info_name

    class Meta:

        verbose_name = 'Пункт информации'
        verbose_name_plural = 'Пукнты информации'

# Блок "Услуги"

class Service(models.Model):
    # Основная модель услуг

    name = models.CharField('Наименование', 
                            max_length=60,  
                            unique=True
                            )
    short_desc = models.TextField('Краткое описание')
    description = models.TextField('Описание')

    def __str__(self):
        return "Услуга: " + self.name

    class Meta:

        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class ServiceWorksNames(models.Model):
    # Наименования работ для конкретной услуги

    service_name = models.ForeignKey(Service, 
                                    #to_field='name', 
                                    on_delete=models.CASCADE
                                    )
    work_title = models.CharField('Наименование работы', 
                                max_length=50, 
                                )
    min_price = models.SmallIntegerField('Минимальная цена')

    def __str__(self):
        return f"{self.service_name.name}: {self.work_title}"

    class Meta:

        verbose_name = 'Наименование работы'
        verbose_name_plural = 'Наименование работ'

class SpecialService(models.Model):
    # Основная модель спец. услуг

    name = models.CharField('Наименование', 
                            max_length=60, 
                            unique=True, 
                            )
    short_desc = models.TextField('Краткое описание')
    description = models.TextField('Описание')

    def __str__(self):
        return "Спец. услуга: " + self.name

    class Meta:

        verbose_name = 'Спец. Услуга'
        verbose_name_plural = 'Спец. Услуги'

class SpecialServiceWorksNames(models.Model):
    # Наименования работ для конкретной спец. услуги

    PRICE_TYPE = "Цена, колич-во и ед. измерения"
    TEXT_TYPE = "Текст"

    INPUT_CHOISES = (
                    (PRICE_TYPE, "Цена, колич-во и ед. измерения"),
                    (TEXT_TYPE, "Текст")
                    )

    service_name = models.ForeignKey(SpecialService, 
                                    on_delete=models.CASCADE
                                    )
    work_title = models.CharField('Наименование работы', 
                                    max_length=50,
                                    )

    input_choice = models.CharField('Тип ячейки', max_length=30, 
                                    choices=INPUT_CHOISES, default=PRICE_TYPE
                                    )
    min_price = models.SmallIntegerField('Минимальная цена',
                                        blank=True,
                                        null=True
                                        )
    count = models.SmallIntegerField('Количество', blank=True, null=True)
    units = models.CharField('Ед. измерения', 
                            max_length=10, 
                            blank=True,
                            null=True
                            )
    alternate_text = models.TextField('Альтернативный текст', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Разделение на тип ячейки

        if self.input_choice == self.PRICE_TYPE:
            if self.alternate_text:
                raise ValidationError('Альтернативный текст должен быть пустым')
            elif not (self.min_price or self.count or self.units):
                raise ValidationError('Есть незаполненные поля')
                    
        else:
            if self.min_price or self.count or self.units:
                raise ValidationError('Должен присутсвовать только альтернативный текст')
                    
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.service_name.name}: {self.work_title}"

    class Meta:

        verbose_name = 'Наименование спец. работы'
        verbose_name_plural = 'Наименование спец. работ'

# Блок "Почему мы"

class WhyWe(models.Model):
    # Модель элемента для блока "Почему мы"

    name = models.CharField('Название элемента', max_length=30)
    #image_for_name = models.ImageField('Фон для названия', upload_to="images/whywe/name")
    description = models.TextField('Описание элемента')
    #image_for_description = models.ImageField('Фон для описания', upload_to="images/whywe/description")

    def __str__(self):
        return f"Пункт: {self.name}"

    class Meta:

        verbose_name = 'Почему мы'
        verbose_name_plural = 'Почему мы'

# Блок "Как мы работаем"

class OrderRequest(models.Model):
    # Модель запроса на заказ

    name = models.CharField('Имя', max_length=20)
    phone = models.CharField('Номер телефона', max_length=20)
    email = models.CharField('Эл. почта', max_length=20)
    date = models.DateField('Дата заказа', auto_now_add=True)

    def __str__(self):
        return f"Заказ: {self.name} ({self.date})"

    class Meta:

        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

# Блок "Отзывы"

class Reviews(models.Model):
    # Модель отзыва

    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Фамилия', max_length=20)
    #reviewer_photo = models.ImageField('Фото', upload_to="images/review")
    review_text = models.TextField('Отзыв')
    approved = models.BooleanField('Одобрен', default=False)
    date = models.DateField('Дата написания', auto_now_add=True)

    def __str__(self):
        return f"Отзыв: {self.first_name} {self.last_name} ({self.date})"

    class Meta:

        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

