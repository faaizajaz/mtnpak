from django import template
from utils.conversions import convert_units
#from grades.models import Grade

register = template.Library()

@register.filter(name='grade_display')
#the filter function takes two arguments, the grade object and request
def grade_display(grade, request):
	
	#Try reading the request.session variable for user pref
	try:
		grade_pref = request.session['grade_pref']
	#if no user logged in, then default to french
	except KeyError:
		grade_pref = 'French'

	#return the correct grade field to display in template
	if grade_pref == 'French':
		return grade.ggrade
	elif grade_pref == 'YDS':
		return grade.ydsgrade
	elif grade_pref == 'Aus':
		return grade.ausgrade
	elif grade_pref == 'UIAA':
		return grade.uiaagrade
	elif grade_pref == 'SA':
		return grade.sagrade
	elif grade_pref == 'UK':
		return grade.ukgrade
	else:
		return grade.ggrade


#filter to change how units are displayed (feet or meter)
@register.filter(name='measurement_unit_display')
def measurement_unit_display(pitch, request):

	try:
		measurement_pref = request.session['measurement_pref']
	#if no user logged in, then default to meters
	except KeyError:
		measurement_pref = 'meters'

	if measurement_pref == pitch.pbase_unit:
		return measurement_pref
	else:
		if measurement_pref == 'meters':
			return measurement_pref
		elif measurement_pref == 'feet':
			return measurement_pref

#filter to change how actual measurements are displayed (in which unit)
#this filter calls a conversion helper function to decide how to convert
@register.filter(name='measurement_display')
def measurement_display(pitch, request):
	try:
		measurement_pref = request.session['measurement_pref']
	#if no user logged in, then default to meters
	except KeyError:
		measurement_pref = 'meters'	

	return convert_units(pitch.pbase_unit, measurement_pref, pitch.plength)



