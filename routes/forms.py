from django.forms import ModelForm
from ascents.models import Ascent




class AddAscentToRouteForm(ModelForm):

	class Meta:
		model = Ascent
		#fields = ['route', 'climber', 'date']
		exclude = ['climber', 'route']

