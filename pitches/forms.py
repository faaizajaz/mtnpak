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

