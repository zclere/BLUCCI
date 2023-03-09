from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

def magazines(request):

	filtered_user = User.objects.get(username="blucci")
	
	if request.user.is_authenticated:
		magazines = Magazine.objects.filter(user=request.user).order_by('-id')
	else:
		magazines = Magazine.objects.filter(user=filtered_user).order_by('-id')

	if request.user.is_authenticated:
		genre = Genre.objects.filter(user=request.user).order_by('-id')
	else:
		genre = Genre.objects.filter(user=filtered_user).order_by('-id')


	prefix_genre_fill = request.GET.get('genre_fill')

	if prefix_genre_fill is not None:
		genre_fill_query = prefix_genre_fill.replace("#", "")

		if genre_fill_query != '' and genre_fill_query is not None:
			magazines = magazines.filter(magazine_type__name=genre_fill_query)


	context = {"magazines": magazines, "genre": genre}

	return render(request, 'magazine/magazines.html', context)




def contents(request, magazine_slug):

	magazines = Magazine.objects.get(magazine_slug=magazine_slug)

	contentlist = ContentList.objects.filter(magazine=magazines)

	sort_by = request.GET.get('sort_by')

	if sort_by == '#Latest':
		contentlist = ContentList.objects.filter(magazine=magazines).order_by('-id')

	elif sort_by == '#Oldest':
		contentlist = ContentList.objects.filter(magazine=magazines).order_by('id')


	context = {"contentlist": contentlist, "magazines": magazines}

	return render(request, 'magazine/content_list.html', context)




def detailed_magazine(request, magazine_slug, content_slug):

	contentlist = ContentList.objects.get(content_slug=content_slug)

	detailed_magazine = DetailedMagazine.objects.filter(contentlist=contentlist)



	context = {"detailed_magazine": detailed_magazine, "contentlist": contentlist}

	return render(request, 'magazine/detailed_magazine.html', context)