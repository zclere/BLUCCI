from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from django.contrib.auth import logout, authenticate, login
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib import messages


@login_required(login_url='account:signin')
def my_account(request):

	return render(request, 'account/my_account.html')



def signup(request):
	if request.user.is_authenticated:
		return redirect('account:my_account')

	user_form = UserForm(request.POST or None)
	profile_form = ProfileForm(request.POST or None)

	total_user = User.objects.all()


	if request.method == "POST":
		if all([user_form.is_valid(), profile_form.is_valid()]):
			if not total_user.count() >= 2:
				parent = user_form.save(commit=False)
				parent.is_staff = True
				parent.save()
				group = Group.objects.get(name='editor')
				parent.groups.add(group)
				child = profile_form.save(commit=False)
				child.user = parent
				child.save()


				#retrieves the data from the form in a safe way
				username = user_form.cleaned_data['username']
				password = user_form.cleaned_data['password1']

				#verifies the user
				user = authenticate(username=username, password=password)
				
				#actually logs the user in
				login(request, user)
				messages.info(request, f"Account created for {username}")
				return redirect("magazine:magazines")

			else:
				#WIP
				messages.info(request, f"User creation limit exceeded. Please follow as instructed!")
				return redirect("option:option")



	context = {
		'user_form': user_form,
		'profile_form': profile_form
	}

	return render(request, 'account/create_account.html', context)


def signin(request):
	if request.user.is_authenticated:
		return redirect('account:my_account')

	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('magazine:magazines')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")

	form = AuthenticationForm()

	context = {
		'form': form
	}

	return render(request, 'account/login.html', context)


def signout(request):
	logout(request)
	messages.info(request, f"Logged out successfully")
	return redirect('account:signin')