from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserPrefsForm
from django.contrib.auth.models import User

#view for updating user prefs
@login_required
def UpdateUserPrefs(request, **kwargs):

	instance = User.objects.get(username=kwargs['username']).userpref

	if request.method == 'POST':
		form = UpdateUserPrefsForm(request.POST, instance = instance)
		if form.is_valid():
			#newpref = form.save(commit=False)
			#newpref.user = request.user
			form.save()
			return redirect('profile', username=kwargs['username'])
	else:
		form = UpdateUserPrefsForm(instance = instance)
	return render(request, 'users/editprefs.html', {'form': form})