from django.shortcuts import render


def option(request):
	return render(request, 'option/options.html')