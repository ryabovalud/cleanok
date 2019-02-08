from django.shortcuts import render
from main.models import *


# Create your views here.

def index(request):

	qs_short_info = ShortInfoAboutCompany.objects.all()[0]

	qs_info_item = InfoItem.objects.all()

	qs_service = Service.objects.all()

	# qs_whywe = WhyWe.objects.all()

	return render(request, 'main.html', {'short_info': qs_short_info, 'info_item': qs_info_item, 
										  'service': qs_service, # 'whywe': qs_whywe
										})