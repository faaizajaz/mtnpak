from django import forms
from django.forms import ModelForm
from .models import Pitch

class AddPitchForm(ModelForm):

	class Meta:
		model = Pitch