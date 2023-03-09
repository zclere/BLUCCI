from django.shortcuts import render
from magazine.models import *
from .models import *
# Create your views here.

def home(request):

	filtered_user = User.objects.get(username="blucci")

	if request.user.is_authenticated:
		filtered_content_list = ContentList.objects.filter(user=request.user)
		most_recent_cl = filtered_content_list.last()
		detailed_mag = DetailedMagazine.objects.filter(contentlist=most_recent_cl)
		firsttitle = detailed_mag.first()

		feature_c = FeaturedContent.objects.filter(user=request.user)

	else:
		filtered_content_list = ContentList.objects.filter(user=filtered_user)
		most_recent_cl = filtered_content_list.last()
		detailed_mag = DetailedMagazine.objects.filter(contentlist=most_recent_cl)
		firsttitle = detailed_mag.first()

		feature_c = FeaturedContent.objects.filter(user=filtered_user)



	context = {"most_recent_cl": most_recent_cl, "firsttitle": firsttitle, "feature_c": feature_c}

	return render(request, 'home/home.html', context)