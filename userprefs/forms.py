from django import forms
from django.forms import ModelForm
from .models import UserPref

class UpdateUserPrefsForm(ModelForm):

	grade_pref = forms.CharField(required=True, max_length=50)
	grade_pref.label = "Choose the grading system you want displayed"
	measurement_pref = forms.CharField(required=True, max_length=50)
	measurement_pref.label = "Choose your measurement preference"

	class Meta:
		model = UserPref
		fields = ['grade_pref', 'measurement_pref']