from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


User = get_user_model()

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)

YEARS= [x for x in range(1940,2021)]

class UserForm(UserCreationForm):
    password2 = None
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

class ProfileForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=YEARS), required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(), required=True)
    class Meta:
        model = Profile
        fields = ('birthday', 'gender')
