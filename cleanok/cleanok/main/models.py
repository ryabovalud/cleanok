from django.db import models

# Create your models here.

# Блок "О нашей компании"

class ShortInfoAboutCompany(models.Model):

	text_about = models.TextField()

class InfoItem(models.Model):

	info_name = models.CharField(max_length=20, unique=True)
	info_description = models.TextField()

# Блок "Услуги"

class Service(models.Model):

	name = models.CharField(max_length=30, unique=True)
	short_desc = models.TextField()
	description = models.TextField()

class ServiceWorksNames(models.Model):

	service_name = models.ForeignKey(Service, to_field='name', on_delete=models.CASCADE)
	work_title = models.CharField(max_length=50)
	min_price = models.SmallIntegerField()

# Блок "Почему мы"

class WhyWe(models.Model):

	name = models.CharField(max_length=30)
	#image_for_name =
	description = models.TextField()
	#image_for_description = 

# Блок "Как мы работаем"

class OrderRequest(models.Model):

	name = models.CharField(max_length=20)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=20)

# Блок "Отзывы"

class Reviews(models.Model):

	name = models.CharField(max_length=35)
	#reviewer_photo = 
	review_text = models.TextField()