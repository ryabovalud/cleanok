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
		qs_services = Service.objects.all()
		qs_worksnames = ServiceWorksNames.objects.all()
		qs_special_services = SpecialService.objects.all()
		qs_special_worknames = SpecialServiceWorksNames.objects.all()
		qs_whywe = WhyWe.objects.all()
		qs_reviews = Reviews.objects.all()

		#Форма запроса на заказ
		order_form = OrderRequestForm()
		review_form = ReviewForm()

                #Форма оставления отзыва
		review_form = ReviewForm()

		context = {'short_info': qs_short_info, 'info_item': qs_info_item, 
					'services': qs_services, 'worksnames': qs_worksnames,
					'special_services': qs_special_services,
					'special_worksnames': qs_special_worknames,
					'whywe': qs_whywe, 'reviews': qs_reviews, 
					'order_form': order_form, 'review_form': review_form,
					}

		return render(request, 'main/main.html', context)

	def post(self, request):

		# Обработка формы заказа
		if 'order_form' in request.POST:
			form = OrderRequestForm(request.POST)
			if form.is_valid():
				new = OrderRequest(**form.cleaned_data)
				new.save()
		# Обработка формы отзыва
		elif 'review_form' in request.POST:
			form = ReviewForm(request.POST)
			if form.is_valid():
				new = Reviews(**form.cleaned_data)
				new.save()

		return HttpResponseRedirect('/')
