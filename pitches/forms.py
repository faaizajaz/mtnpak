from django import forms
from django.forms import ModelForm
from .models import Pitch

#This is the single pitch class.
class AddPitchForm(ModelForm):

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']

#use this form for adding pitches to multipitch
class AddPitchMultiForm(ModelForm):

	class Meta:
		model = Pitch
		exclude = ['proute']


