from django.forms import ModelForm
from grades.models import Grade
from .fields import *    
from .models import Pitch

#for singlepitch forms
class AddPitchFormYDS(ModelForm):		
	grade = YDSModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'base_unit']

class AddPitchFormFrench(ModelForm):
	grade = FrenchModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'base_unit']

class AddPitchFormAus(ModelForm):
	grade = AusModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'base_unit']

class AddPitchFormUIAA(ModelForm):
	grade = UIAAModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'base_unit']

class AddPitchFormSA(ModelForm):
	grade = SAModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'base_unit']

class AddPitchFormUK(ModelForm):
	grade = UKModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'base_unit']



#For multipitch forms
class AddPitchFormYDSMulti(ModelForm):		
	grade = YDSModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'base_unit']

class AddPitchFormFrenchMulti(ModelForm):
	grade = FrenchModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'base_unit']

class AddPitchFormAusMulti(ModelForm):
	grade = AusModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'base_unit']

class AddPitchFormUIAAMulti(ModelForm):
	grade = UIAAModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'base_unit']

class AddPitchFormSAMulti(ModelForm):
	grade = SAModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'base_unit']

class AddPitchFormUKMulti(ModelForm):
	grade = UKModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'base_unit']
