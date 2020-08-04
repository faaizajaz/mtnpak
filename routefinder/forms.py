from django import forms
from pitches.fields import YDSModelChoiceField, FrenchModelChoiceField
from grades.models import Grade

class RouteFinderFormYDS(forms.Form):
	TYPE_CHOICES = (
	('Sport', 'Sport'),
	('Trad', 'Trad'),
	('Mixed', 'Mixed'),
	)

	max_grade = YDSModelChoiceField(queryset=Grade.objects.all())
	route_type = forms.ChoiceField(choices=TYPE_CHOICES)

class RouteFinderFormFrench(forms.Form):
	TYPE_CHOICES = (
	('Sport', 'Sport'),
	('Trad', 'Trad'),
	('Mixed', 'Mixed'),
	)

	max_grade = FrenchModelChoiceField(queryset=Grade.objects.all())
	route_type = forms.ChoiceField(choices=TYPE_CHOICES)


