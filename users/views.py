from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


def RegisterUser(request):

	# if request is POST (register button submitted) make user creation
	# form with post data, otherwise just create  blank form.
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			#upon successgul login, redirect to login page.
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form': form})



#USED MIXIN TO MAKE LOGIN MANDATORY
class UserProfile(LoginRequiredMixin, generic.DetailView):

	#if not logged in, redirect to here to login
	login_url='/login/'

	template_name = 'users/profile.html'
	model = User

	def get_object(self):
		return get_object_or_404(User, username=self.kwargs['username'])


@login_required
def EditProfile(request, **kwargs):

	instance = User.objects.get(username=kwargs['username'])

	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			return redirect('profile', username=kwargs['username'])
	else:
		user_form = UserUpdateForm(instance=instance)
	return render(request, 'users/editprofile.html', {'user_form': user_form})


		
