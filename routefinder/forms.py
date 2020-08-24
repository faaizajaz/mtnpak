from django import forms
from django.forms import ModelForm
from .models import RoutefinderQuery
from grades.models import Grade
from cities.models import City
from pitches.fields import *
from leaflet.forms.widgets import LeafletWidget
from djgeojson.fields import GeoJSONFormField

class RouteFinderFormFrench(ModelForm):
	TYPE_CHOICES = (
		('Any', 'Any'),
		('Sport', 'Sport'),
		('Trad', 'Trad'),
		('Mixed', 'Mixed'),
	)

	TOPROPE_CHOICES = (
		('Any', 'Any'),
		('Must have toprope access', 'Must have toprope access'),
	)

	route_type = forms.ChoiceField(choices=TYPE_CHOICES)
	max_grade = FrenchModelChoiceField(queryset=Grade.objects.all(), empty_label="Any", required=False)
	city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="Any", required=False)
	toprope = forms.ChoiceField(choices=TOPROPE_CHOICES)
	location = GeoJSONFormField(geom_type='POINT')

	class Meta:
		LEAFLET_WIDGET_ATTRS = {
			'map_height': '500px',
			'map_width': '500px',
		}

		model = RoutefinderQuery
		exclude = ['user']
		widgets = {'location': LeafletWidget(LEAFLET_WIDGET_ATTRS)}


class RouteFinderFormYDS(ModelForm):
	TYPE_CHOICES = (
		('Any', 'Any'),
		('Sport', 'Sport'),
		('Trad', 'Trad'),
		('Mixed', 'Mixed'),
	)
	
	TOPROPE_CHOICES = (
		('Any', 'Any'),
		('Must have toprope access', 'Must have toprope access'),
	)

	route_type = forms.ChoiceField(choices=TYPE_CHOICES)
	max_grade = YDSModelChoiceField(queryset=Grade.objects.all(), empty_label="Any", required=False)
	city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="Any", required=False)
	toprope = forms.ChoiceField(choices=TOPROPE_CHOICES)
	location = GeoJSONFormField(geom_type='POINT')

	class Meta:
		LEAFLET_WIDGET_ATTRS = {
			'map_height': '500px',
			'map_width': '500px',
		}
		model = RoutefinderQuery
		exclude = ['user']
		widgets = {'location': LeafletWidget(LEAFLET_WIDGET_ATTRS)}


