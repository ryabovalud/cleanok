from django.shortcuts import render
from main.models import *
from collections import defaultdict

# Create your views here.

def index(request):

	qs_short_info = ShortInfoAboutCompany.objects.all()[0]

	qs_info_item = InfoItem.objects.all()

	qs_service = Service.objects.all()

	qs_worksnames = ServiceWorksNames.objects.all()

	combined_worknames = combine_items(qs_worksnames)

	print(combined_worknames)

	return render(request, 'main.html', {'short_info': qs_short_info, 'info_item': qs_info_item, 
										  'service': qs_service, 'combined': combined_worknames
										})

def combine_items(q_set):

	combined = defaultdict(list)

	for item in q_set:
		combined[item.min_price].append(item.work_title)

	return combined