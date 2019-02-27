from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from collections import defaultdict

# Create your views here.

class MainView(View):

	def get(self, request):

		#QuerySet'ы объектов
		qs_short_info = ShortInfoAboutCompany.objects.first()
		qs_info_item = InfoItem.objects.all()
		qs_service = Service.objects.all()
		qs_worksnames = ServiceWorksNames.objects.all()
		qs_special_service = SpecialService.objects.all()
		qs_special_worknames = SpecialServiceWorksNames.objects.all()
		qs_whywe = WhyWe.objects.all()
		qs_reviews = Reviews.objects.all()

		#Форма запроса на заказ
		order_form = OrderRequestForm()

                #Форма оставления отзыва
		review_form = ReviewForm()

		context = {'short_info': qs_short_info, 'info_item': qs_info_item, 
					'service': qs_service, 'worknames': qs_worksnames,
					'special_service': qs_special_service,
					'special_worknames': qs_special_worknames,
					'whywe': qs_whywe, 'reviews': qs_reviews, 
					'order_form': order_form, 'review_form': review_form,
					}

		return render(request, 'main/main.html', context)

	def post(self, request):

		# Определяем, с какой формы пришёл запрос
		form_name = list(request.POST)[-1]

		# Обработка формы заказа
		if form_name == 'order_form':
			form = OrderRequestForm(request.POST)
			if form.is_valid():
				new = OrderRequest(**form.cleaned_data)
				new.save()
		# Обработка формы отзыва
		else:
			form = ReviewForm(request.POST)
			if form.is_valid():
				new = Reviews(**form.cleaned_data)
				new.save()

		return HttpResponse('<p>Good</p>')
