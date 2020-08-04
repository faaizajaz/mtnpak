from django import forms
from django.forms import ModelForm
from routes.models import Route
from .models import Crag
from leaflet.forms.widgets import LeafletWidget
from cities.models import City




#this is the single pitch add route form. It displays along wiht pitch form
class AddRouteForm(ModelForm):

	
	CHOICES = (
		('Sport', 'Sport'),
		('Trad', 'Trad'),
		('Mixed', 'Mixed'),
		)
	rtype = forms.ChoiceField(choices=CHOICES)
	#rname = forms.CharField()
	#rname.widget.attrs.update({'placeholder': 'something studddpfffid', 'rows':40})

	class Meta:
		model = Route
		fields = ('rname', 'rdescription', 'rtype',)
		#rlength is set equal to pitch length once pitch is created
		#exclude = ['rcrag', 'ropener', 'numpitch', 'length', 'base_unit', 'avg_rating', 'grade']


class AddRouteMultiForm(ModelForm):
	CHOICES = (
		('Sport', 'Sport'),
		('Trad', 'Trad'),
		('Mixed', 'Mixed'),
		)
	rtype = forms.ChoiceField(choices=CHOICES)

	class Meta:
		model = Route
		exclude = ['rcrag', 'ropener', 'length', 'numpitch', 'base_unit', 'avg_rating', 'grade']




class RouteChoiceForm(forms.Form):
	CHOICES = (
		('single', 'single'),
		('multi', 'multi')
		)
	choice = forms.ChoiceField(choices=CHOICES)



class AddCragForm(ModelForm):

	#city = forms.ModelChoiceField(City.objects.all())

	class Meta:
		LEAFLET_WIDGET_ATTRS = {
			'map_height': '500px',
			'map_width': '500px',
		}
		model = Crag
		exclude = ['cauthor', 'city']
		widgets = {'location': LeafletWidget(LEAFLET_WIDGET_ATTRS)}
