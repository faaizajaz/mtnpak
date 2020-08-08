from django import forms
from pitches.fields import YDSModelChoiceField, FrenchModelChoiceField
from grades.models import Grade
from cities.models import City
from django.forms import ModelChoiceField





class RouteFinderFormYDS(forms.Form):
	TYPE_CHOICES = (
	('Sport', 'Sport'),
	('Trad', 'Trad'),
	('Mixed', 'Mixed'),
	)

	max_grade = YDSModelChoiceField(queryset=Grade.objects.all())
	route_type = forms.ChoiceField(choices=TYPE_CHOICES)
	city = ModelChoiceField(queryset=City.objects.all())


class RouteFinderFormFrench(forms.Form):
	TYPE_CHOICES = (
	('Sport', 'Sport'),
	('Trad', 'Trad'),
	('Mixed', 'Mixed'),
	)

	max_grade = FrenchModelChoiceField(queryset=Grade.objects.all(), empty_label="Any", required=False)
	route_type = forms.ChoiceField(choices=TYPE_CHOICES)
	city = ModelChoiceField(queryset=City.objects.all())





# first add map input to this form.


