from django.forms import ModelForm
from grades.models import Grade
from .fields import *    
from .models import Pitch

#for singlepitch forms
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



#For multipitch forms
class AddPitchFormYDSMulti(ModelForm):		
	pgrade = YDSModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']

class AddPitchFormFrenchMulti(ModelForm):
	pgrade = FrenchModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']

class AddPitchFormAusMulti(ModelForm):
	pgrade = AusModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']

class AddPitchFormUIAAMulti(ModelForm):
	pgrade = UIAAModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']

class AddPitchFormSAMulti(ModelForm):
	pgrade = SAModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']

class AddPitchFormUKMulti(ModelForm):
	pgrade = UKModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']
