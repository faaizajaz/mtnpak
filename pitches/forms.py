from django.forms import ModelForm
from grades.models import Grade
from .fields import *

    
from .models import Pitch

#This is the single pitch class.
class AddPitchFormYDS(ModelForm):
	#override init method so that I can access request here.
		
	pgrade = YDSModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']

class AddPitchFormFrench(ModelForm):
	#override init method so that I can access request here.

	pgrade = FrenchModelChoiceField(queryset=Grade.objects.all())

	class Meta:
		model = Pitch
		exclude = ['proute', 'pdescription']


#use this form for adding pitches to multipitch
class AddPitchMultiForm(ModelForm):

	class Meta:
		model = Pitch
		exclude = ['proute']
