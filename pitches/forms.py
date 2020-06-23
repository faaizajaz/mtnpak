from django import forms
from django.forms import ModelForm
from .models import Pitch

#This is the single pitch class. There is none for multi
class AddPitchForm(ModelForm):

	class Meta:
		model = Pitch
		exclude = ['proute']


