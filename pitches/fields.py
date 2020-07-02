from django.forms import ModelChoiceField

##Make a bunch of field classes for each different grade type.

class YDSModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.ydsgrade

class FrenchModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.ggrade