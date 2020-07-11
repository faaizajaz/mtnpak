from django import template
from utils.conversions import convert_units
from django.utils.safestring import mark_safe
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
	return measurement_pref

#filter to change how actual measurements are displayed (in which unit)
#this filter calls a conversion helper function to decide how to convert
@register.filter(name='measurement_display')
def measurement_display(obj, request):
	try:
		measurement_pref = request.session['measurement_pref']
	#if no user logged in, then default to meters
	except KeyError:
		measurement_pref = 'meters'	
	return convert_units(obj.base_unit, measurement_pref, obj.length)

@register.filter(name='inline_rating')
def inline_rating(route):
	percentage_rating = (route.avg_rating*100)//5

	if percentage_rating == 0:
		return mark_safe('<span class="score s0"></span>')

	elif percentage_rating >= 0 and percentage_rating < 11:
		
		return mark_safe('<span class="score s1"></span>')

	elif percentage_rating >= 11 and percentage_rating < 21:
		
		return mark_safe('<span class="score s2"></span>')

	elif percentage_rating >= 21 and percentage_rating < 31:
		
		return mark_safe('<span class="score s3"></span>')

	elif percentage_rating >= 31 and percentage_rating < 41:
		
		return mark_safe('<span class="score s4"></span>')

	elif percentage_rating >= 41 and percentage_rating < 51:
		
		return mark_safe('<span class="score s5"></span>')

	elif percentage_rating >= 51 and percentage_rating < 61:
		
		return mark_safe('<span class="score s6"></span>')

	elif percentage_rating >= 61 and percentage_rating < 71:
		
		return mark_safe('<span class="score s7"></span>')

	elif percentage_rating >= 71 and percentage_rating < 81:
		
		return mark_safe('<span class="score s8"></span>')

	elif percentage_rating >= 81 and percentage_rating < 91:
		
		return mark_safe('<span class="score s9"></span>')

	elif percentage_rating >= 91 and percentage_rating <= 100:
		
		return mark_safe('<span class="score s10"></span>')

	else:
		return("ERROR")


@register.filter(name='inline_user_rating')
def inline_user_rating(route, user):

	if route.rating_set.filter(user=user).count() > 0:

		user_percentage_rating = (route.rating_set.get(user=user).score*100)//5

		if user_percentage_rating == 0:

			return mark_safe('<span class="score s0"></span>')

		elif user_percentage_rating >= 0 and user_percentage_rating < 11:
			
			return mark_safe('<span class="score s1"></span>')

		elif user_percentage_rating >= 11 and user_percentage_rating < 21:
			
			return mark_safe('<span class="score s2"></span>')

		elif user_percentage_rating >= 21 and user_percentage_rating < 31:
			
			return mark_safe('<span class="score s3"></span>')

		elif user_percentage_rating >= 31 and user_percentage_rating < 41:
			
			return mark_safe('<span class="score s4"></span>')

		elif user_percentage_rating >= 41 and user_percentage_rating < 51:
			
			return mark_safe('<span class="score s5"></span>')

		elif user_percentage_rating >= 51 and user_percentage_rating < 61:
			
			return mark_safe('<span class="score s6"></span>')

		elif user_percentage_rating >= 61 and user_percentage_rating < 71:
			
			return mark_safe('<span class="score s7"></span>')

		elif user_percentage_rating >= 71 and user_percentage_rating < 81:
			
			return mark_safe('<span class="score s8"></span>')

		elif user_percentage_rating >= 81 and user_percentage_rating < 91:
			
			return mark_safe('<span class="score s9"></span>')

		elif user_percentage_rating >= 91 and user_percentage_rating <= 100:
			
			return mark_safe('<span class="score s10"></span>')

		else:
			return("ERROR")


@register.filter(name='get_rating_count')
def get_rating_count(route, user):
	return route.rating_set.filter(user=user).count()







