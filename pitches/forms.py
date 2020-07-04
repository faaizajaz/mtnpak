from django.forms import ModelForm
from grades.models import Grade
from .fields import *    
from .models import Pitch

#for singlepitch forms
class AddPitchFormYDS(ModelForm):		
	pgrade = YDSModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'pbase_unit']

class AddPitchFormFrench(ModelForm):
	pgrade = FrenchModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'pbase_unit']

class AddPitchFormAus(ModelForm):
	pgrade = AusModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'pbase_unit']

class AddPitchFormUIAA(ModelForm):
	pgrade = UIAAModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'pbase_unit']

class AddPitchFormSA(ModelForm):
	pgrade = SAModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'pbase_unit']

class AddPitchFormUK(ModelForm):
	pgrade = UKModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'pbase_unit']



#For multipitch forms
class AddPitchFormYDSMulti(ModelForm):		
	pgrade = YDSModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'pbase_unit']

class AddPitchFormFrenchMulti(ModelForm):
	pgrade = FrenchModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'pbase_unit']

class AddPitchFormAusMulti(ModelForm):
	pgrade = AusModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'pbase_unit']

class AddPitchFormUIAAMulti(ModelForm):
	pgrade = UIAAModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'pbase_unit']

class AddPitchFormSAMulti(ModelForm):
	pgrade = SAModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'pbase_unit']

class AddPitchFormUKMulti(ModelForm):
	pgrade = UKModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription', 'pbase_unit']
