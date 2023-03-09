from django.urls import path
from . import views

app_name = 'siteinfo'

urlpatterns = [
    path('contact', views.contact, name="contact"),
    path('terms&conditions', views.terms, name="terms"),
    path('privacy', views.privacy, name="privacy"),
]