from django import forms
from django.forms import ModelForm
from routes.models import Route
from .models import Crag
from routetypes.models import RouteType

#this is the single pitch add route form. It displays along wiht pitch form
class AddRouteForm(ModelForm):

	rtype = forms.ModelChoiceField(queryset=RouteType.objects.all(), empty_label="select type")

	class Meta:
		model = Route
		#rlength is set equal to pitch length once pitch is created
		exclude = ['rcrag', 'ropener', 'numpitch', 'rlength', 'rbase_unit']


class AddRouteMultiForm(ModelForm):

	class Meta:
		model = Route
		exclude = ['rcrag', 'ropener', 'rlength', 'numpitch', 'rbase_unit']




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

