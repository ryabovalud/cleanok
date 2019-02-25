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
		qs_short_info = ShortInfoAboutCompany.objects.get(pk=1)
		qs_info_item = InfoItem.objects.all()
		qs_service = Service.objects.all()
		qs_worksnames = ServiceWorksNames.objects.all()
		qs_special_service = SpecialService.objects.all()
		qs_special_worknames = SpecialServiceWorksNames.objects.all()
		qs_whywe = WhyWe.objects.all()
		qs_reviews = Reviews.objects.all()

		#Формы заказов и отзывов
		order_form = OrderRequestForm()
		review_form = ReviewForm()

		return render(request, 'main/main.html', {'short_info': qs_short_info, 
												'info_item': qs_info_item, 
										  		'service': qs_service,
										  		'worknames': qs_worksnames,
										  		'special_service': qs_special_service,
										  		'special_worknames': qs_special_worknames,
										  		'whywe': qs_whywe,
										  		'reviews': qs_reviews,
										  		'order_form': order_form,
										  		'review_form': review_form
												})

	"""def post(self, request):
					
					form1 = OrderRequestForm(request.POST)
					form2 = ReviewForm(request.POST)
			
					if OrderRequestForm(request.POST).is_valid():
						data = OrderRequestForm(request.POST).cleaned_data
						print(data)
					elif ReviewForm(request.POST).is_valid():
						data = ReviewForm(request.POST).cleaned_data
						print(data)
					else:
						print('error хуле')
					return HttpResponseRedirect('/')"""


class ReviewView(FormView):
	template_name = 'main/main.html'
	form_class = ReviewForm
	success_url = '/review/'

	def form_valid(self, form):
		print(form.cleaned_data)
		return HttpResponse('Review form success')

class OrderView(FormView):
	template_name = 'main/main.html'
	form_class = OrderRequestForm
	success_url = '/order/'

	def form_valid(self, form):
		print(form.cleaned_data)
		return HttpResponse('Order form success')



"""def index(request):

	qs_short_info = ShortInfoAboutCompany.objects.get(pk=1)

	qs_info_item = InfoItem.objects.all()

	qs_service = Service.objects.all()

	qs_worksnames = ServiceWorksNames.objects.all()
	#print(ShortInfoAboutCompany.objects.values().get(pk=2))
	combined_worknames = combine_items(qs_worksnames)

	return render(request, 'main/main.html', {'short_info': qs_short_info, 'info_item': qs_info_item, 
										  'service': qs_service, 'combined': combined_worknames,
										})

def combine_items(q_set):

	combined = defaultdict(list)

	for item in q_set:
		combined[item.min_price].append(item.work_title)

	return combined"""