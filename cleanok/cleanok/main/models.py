from django.db import models

# Create your models here.

# Блок "О нашей компании"

class ShortInfoAboutCompany(models.Model):

	text_about = models.TextField()

	class Meta:

		verbose_name = 'Краткая информация о компании'
		verbose_name_plural = 'Краткая информация о компании'

class InfoItem(models.Model):

	info_name = models.CharField(max_length=20, unique=True)
	info_description = models.TextField()

	class Meta:

		verbose_name = 'Пункт информации'
		verbose_name_plural = 'Пукнты информации'

# Блок "Услуги"

class Service(models.Model):

	name = models.CharField(max_length=30, unique=True)
	short_desc = models.TextField()
	description = models.TextField()

	class Meta:

		verbose_name = 'Услуга'
		verbose_name_plural = 'Услуги'

class ServiceWorksNames(models.Model):

	service_name = models.ForeignKey(Service, to_field='name', on_delete=models.CASCADE)
	work_title = models.CharField(max_length=50)
	min_price = models.SmallIntegerField()

	class Meta:

		verbose_name = 'Наименование работы'
		verbose_name_plural = 'Наименование работ'

class SpecialService(models.Model):

	name = models.CharField(max_length=40, unique=True)
	short_desc = models.TextField()
	description = models.TextField()

	class Meta:

		verbose_name = 'Спец. Услуга'
		verbose_name_plural = 'Спец. Услуги'

class SpecialServiceWorksNames(models.Model):

	service_name = models.ForeignKey(SpecialService, to_field='name', on_delete=models.CASCADE)
	work_title = models.CharField(max_length=50)
	min_price = models.SmallIntegerField()
	count = models.SmallIntegerField()
	units = models.CharField(max_length=10)

	class Meta:

		verbose_name = 'Наименование спец. работы'
		verbose_name_plural = 'Наименование спец. работ'

# Блок "Почему мы"

class WhyWe(models.Model):

	name = models.CharField(max_length=30)
	#image_for_name = models.ImageField(upload_to="uploads/images/")
	description = models.TextField()
	#image_for_description = models.ImageField(upload_to="uploads/images/")

	class Meta:

		verbose_name = 'Почему мы'
		verbose_name_plural = 'Почему мы'

# Блок "Как мы работаем"

class OrderRequest(models.Model):

	name = models.CharField(max_length=20)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=20)

	class Meta:

		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

# Блок "Отзывы"

class Reviews(models.Model):

	name = models.CharField(max_length=35)
	#reviewer_photo = models.ImageField(upload_to="uploads/images/")
	review_text = models.TextField()

	class Meta:

		verbose_name = 'Отзыв'
		verbose_name_plural = 'Отзывы'