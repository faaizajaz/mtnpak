from django import forms
from django.forms import ModelForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from routes.models import Route
from .models import Crag
from routetypes.models import RouteType

#this is the single pitch add route form.
class AddRouteForm(ModelForm):

	rtype = forms.ModelChoiceField(queryset=RouteType.objects.all(), empty_label="select type")

	class Meta:
		model = Route
		exclude = ['rcrag', 'ropener', 'numpitch', 'rlength']


class AddRouteMultiForm(ModelForm):

	class Meta:
		model = Route
		exclude = ['rcrag', 'ropener', 'rlength', 'numpitch']




class RouteChoiceForm(forms.Form):
	CHOICES = (
		('single', 'single'),
		('multi', 'multi')
		)
	choice = forms.ChoiceField(choices=CHOICES)



class AddCragForm(ModelForm):
	class Meta:
		model = Crag
		exclude = ['cauthor']

