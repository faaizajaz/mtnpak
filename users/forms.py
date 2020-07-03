from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, UserPref


#here we are extending the usercreation form to add some additional fields
# Add any other fields you want here
class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	firstname = forms.CharField(required=True, max_length=200)
	lastname = forms.CharField(required=True, max_length=200)
	firstname.label = "First Name"
	lastname.label = "Last Name"

	#Keeps configuratons in one place
	class Meta:
		# When form validates, User object is created (form.save will save to user model)
		# the model we want it to interact with is User (remember, models = DBs)
		model = User
		#these are fields and order we want on form
		fields = ['username', 'firstname', 'lastname', 'email', 'password1', 'password2']

	def save(self, commit=True):
		user = super(UserRegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['firstname']
		user.last_name = self.cleaned_data['lastname']

		if commit:
			user.save()
		return user


class UserUpdateForm(forms.ModelForm):

	email = forms.EmailField(required=True)
	firstname = forms.CharField(required=True, max_length=200)
	lastname = forms.CharField(required=True, max_length=200)
	firstname.label = "First Name"
	lastname.label = "Last Name"

	class Meta:
		# When form validates, User object is created (form.save will save to user model)
		model = User
		fields = ['firstname', 'lastname', 'username', 'email']




class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']


class UpdateUserPrefsForm(forms.ModelForm):

	class Meta:
		model = UserPref
		fields = ['grade_pref', 'measurement_pref']