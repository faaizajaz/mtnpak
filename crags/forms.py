from django import forms
from django.forms import ModelForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from routes.models import Route
from .models import Crag
from routetypes.models import RouteType


class AddRouteForm(ModelForm):

	rtype = forms.ModelChoiceField(queryset=RouteType.objects.all(), empty_label="select type")

	class Meta:
		model = Route
		exclude = ['rcrag', 'ropener']




class AddCragForm(ModelForm):
	class Meta:
		model = Crag
		exclude = ['cauthor']

