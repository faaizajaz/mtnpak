from django import template
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

