from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, UpdateUserPrefsForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
import pytz
from django.conf import settings


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



#This still does not check to see if current user is same as that to edit.
@login_required
def EditProfile(request, **kwargs):

	#if i do this like request.user.profile is it safer?

	u_instance = User.objects.get(username=kwargs['username'])
	p_instance = User.objects.get(username=kwargs['username']).profile

	if request.method == 'POST':
		#we pass instances here to prepopulate forms with current.
		user_form = UserUpdateForm(request.POST, instance=u_instance)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=p_instance)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()

			#redirect using u_instance.username in case user changes username
			return redirect('profile', username=u_instance.username)
	else:
		user_form = UserUpdateForm(instance=u_instance)
		profile_form = ProfileUpdateForm(instance=p_instance)
	return render(request, 'users/editprofile.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def UpdateUserPrefs(request, **kwargs):

	instance = User.objects.get(username=kwargs['username']).userpref

	if request.method == 'POST':
		form = UpdateUserPrefsForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()

			#Set session variable for grade preference when prefs updated.
			#Also done in users.signals.create_pref_session when session is created
			request.session['grade_pref'] = request.user.userpref.grade_pref
			request.session['measurement_pref'] = request.user.userpref.measurement_pref


			# if timezone_pref is set, activate timezone, else use default.
			if request.user.userpref.timezone_pref:
				request.session['timezone_pref'] = str(request.user.userpref.timezone_pref)
				timezone.activate(pytz.timezone(request.session['timezone_pref']))
			else:
				timezone.activate(pytz.timezone(settings.TIME_ZONE))

			# once saved, redirect to user profile.
			return redirect('profile', username=kwargs['username'])

			
	else:
		form = UpdateUserPrefsForm(instance = instance)
	return render(request, 'users/editprefs.html', {'form': form})