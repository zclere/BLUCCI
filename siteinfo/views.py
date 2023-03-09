from django.shortcuts import render
from .models import *
# Create your views here.


def contact(request):
	return render(request, 'siteinfo/contact.html')


def terms(request):

	try:
		terms = TermsPolicy.objects.get()
	except TermsPolicy.DoesNotExist:
		terms = None

	context = {"terms": terms}


	return render(request, 'siteinfo/terms.html', context)


def privacy(request):

	try:
		privacy = PrivacyPolicy.objects.get()
	except PrivacyPolicy.DoesNotExist:
		privacy = None

	context = {"privacy": privacy}

	return render(request, 'siteinfo/privacy.html', context)