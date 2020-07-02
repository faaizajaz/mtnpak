from django.forms import ModelForm
from grades.models import Grade
from .fields import *

    
from .models import Pitch

#This is the single pitch class.
class AddPitchFormYDS(ModelForm):		
	pgrade = YDSModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']

class AddPitchFormFrench(ModelForm):
	pgrade = FrenchModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']

class AddPitchFormAus(ModelForm):
	pgrade = AusModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']

class AddPitchFormUIAA(ModelForm):
	pgrade = UIAAModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']

class AddPitchFormSA(ModelForm):
	pgrade = SAModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']

class AddPitchFormUK(ModelForm):
	pgrade = UKModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']







#use this form for adding pitches to multipitch
class AddPitchMultiForm(ModelForm):

	class Meta:
		model = Pitch
		exclude = ['proute']
