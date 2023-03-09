from django.urls import path
from . import views

app_name = 'option'

urlpatterns = [
    path('', views.option, name="option"),
]