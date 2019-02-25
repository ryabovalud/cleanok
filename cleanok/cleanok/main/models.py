from django.db import models

# Create your models here.

# Блок "О нашей компании"

class ShortInfoAboutCompany(models.Model):

	text_about = models.TextField('Описание')

	def __str__(self):
		return "Описание"

	class Meta:

		verbose_name = 'Краткая информация о компании'
		verbose_name_plural = 'Краткая информация о компании'

class InfoItem(models.Model):

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

	name = models.CharField('Наименование', 
							max_length=30,  
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

	service_name = models.ForeignKey(Service, 
									to_field='name', 
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

	name = models.CharField('Наименование', 
							max_length=40, 
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

	service_name = models.ForeignKey(SpecialService, 
									to_field='name', 
									on_delete=models.CASCADE
									)
	work_title = models.CharField('Наименование работы', 
									max_length=50, 
									)
	min_price = models.SmallIntegerField('Минимальная цена')
	count = models.SmallIntegerField('Количество')
	units = models.CharField('Ед. измерения', max_length=10)

	def __str__(self):
		return f"{self.service_name.name}: {self.work_title}"

	class Meta:

		verbose_name = 'Наименование спец. работы'
		verbose_name_plural = 'Наименование спец. работ'

# Блок "Почему мы"

class WhyWe(models.Model):

	name = models.CharField('Название элемента', max_length=30)
	#image_for_name = models.ImageField(upload_to="media/images/")
	description = models.TextField('Описание элемента')
	#image_for_description = models.ImageField(upload_to="media/images/")

	def __str__(self):
		return f"Пункт: {self.name}"

	class Meta:

		verbose_name = 'Почему мы'
		verbose_name_plural = 'Почему мы'

# Блок "Как мы работаем"

class OrderRequest(models.Model):

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

	first_name = models.CharField('Имя', max_length=20)
	last_name = models.CharField('Фамилия', max_length=20)
	#reviewer_photo = models.ImageField(upload_to="media/images/review")
	review_text = models.TextField('Отзыв')
	date = models.DateField('Дата написания', auto_now_add=True)

	def __str__(self):
		return f"Отзыв: {self.first_name} {self.last_name} ({self.date})"

	class Meta:

		verbose_name = 'Отзыв'
		verbose_name_plural = 'Отзывы'

