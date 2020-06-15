from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Route
from ascents.models import Ascent
from crags.models import Crag



class AddAscentToRouteForm(ModelForm):

	class Meta:
		model = Ascent
		#fields = ['route', 'climber', 'date']
		exclude = ['climber', 'route']

