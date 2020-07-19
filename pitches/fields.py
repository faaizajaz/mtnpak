from django.forms import ModelChoiceField

#override modelchoice fields to change the __str__
class YDSModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.ydsgrade

class FrenchModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.ggrade

