from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('my_account/', views.my_account, name="my_account"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
]