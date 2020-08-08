from django import forms
from django.forms import ModelForm
from .models import RoutefinderQuery
from grades.models import Grade
from pitches.fields import *
from leaflet.forms.widgets import LeafletWidget






class RouteFinderFormFrench(ModelForm):
	TYPE_CHOICES = (
	('Sport', 'Sport'),
	('Trad', 'Trad'),
	('Mixed', 'Mixed'),
	)

	route_type = forms.ChoiceField(choices=TYPE_CHOICES)
	max_grade = FrenchModelChoiceField(queryset=Grade.objects.all(), empty_label="Any", required=False)

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
	('Sport', 'Sport'),
	('Trad', 'Trad'),
	('Mixed', 'Mixed'),
	)

	route_type = forms.ChoiceField(choices=TYPE_CHOICES)
	max_grade = YDSModelChoiceField(queryset=Grade.objects.all(), empty_label="Any", required=False)

	class Meta:
		LEAFLET_WIDGET_ATTRS = {
			'map_height': '500px',
			'map_width': '500px',
		}
		model = RoutefinderQuery
		exclude = ['user']
		widgets = {'location': LeafletWidget(LEAFLET_WIDGET_ATTRS)}








# first add map input to this form.


