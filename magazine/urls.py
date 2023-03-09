from django.urls import path
from . import views

app_name = 'magazine'

urlpatterns = [
    path('', views.magazines, name="magazines"),
    path('<slug:magazine_slug>', views.contents, name="contents"),
    path('<slug:magazine_slug>/<slug:content_slug>', views.detailed_magazine, name="detailed_magazine"),
]