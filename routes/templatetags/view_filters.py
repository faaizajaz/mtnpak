from django import template
from utils.conversions import convert_units
from django.utils.safestring import mark_safe

#from grades.models import Grade

register = template.Library()

@register.filter(name='grade_display')
#the filter function takes two arguments, the grade/pitch object and request
def grade_display(obj, request):
	
	#Try reading the request.session variable for user pref
	try:
		grade_pref = request.session['grade_pref']
	#if no user logged in, then default to french
	except KeyError:
		grade_pref = 'French'

	#return the correct grade field to display in template
	if grade_pref == 'French':
		return obj.grade.ggrade
	elif grade_pref == 'YDS':
		return obj.grade.ydsgrade

	else:
		return obj.grade.ggrade


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
		return "ERROR"


@register.filter(name='inline_user_rating')
def inline_user_rating(route, user):

	if user.is_authenticated:

		user_rating_count = route.rating_set.filter(user=user).count()

		#If user has not rated the route, show the star rating widget as usual
		if user_rating_count == 0:

			return mark_safe('<div data-api="#" class="rating" id="star-rating">Your rating: \
				<input type="radio" id="star5" name="rating" value="5" data-api="%s"/><label class="full" for="star5" title="5 stars"></label> \
				<input type="radio" id="star4" name="rating" value="4" data-api="%s"/><label class="full" for="star4" title="4 stars"></label> \
				<input type="radio" id="star3" name="rating" value="3" data-api="%s"/><label class="full" for="star3" title="3 stars"></label> \
				<input type="radio" id="star2" name="rating" value="2" data-api="%s"/><label class="full" for="star2" title="2 stars"></label> \
				<input type="radio" id="star1" name="rating" value="1" data-api="%s"/><label class="full" for="star1" title="1 star"></label>\
				</div>'	% (
					
				route.get_api_rate_url(5),
				route.get_api_rate_url(4),
				route.get_api_rate_url(3),
				route.get_api_rate_url(2),
				route.get_api_rate_url(1),	

				))

		#If the user has already rated it, show the widget with the correct number of stars checked
		elif user_rating_count > 0:

			if route.rating_set.filter(user=user).count() > 1:
				return("You are in god mode")
			elif route.rating_set.filter(user=user).count() == 1:
				user_rating = route.rating_set.get(user=user).score


			if user_rating == 1 :
				
				return mark_safe('<div data-api="#" class="rating" id="star-rating">Your rating: \
					<input type="radio" id="star5" name="rating" value="5" data-api="%s"/><label class="full" for="star5" title="5 stars"></label> \
					<input type="radio" id="star4" name="rating" value="4" data-api="%s"/><label class="full" for="star4" title="4 stars"></label> \
					<input type="radio" id="star3" name="rating" value="3" data-api="%s"/><label class="full" for="star3" title="3 stars"></label> \
					<input type="radio" id="star2" name="rating" value="2" data-api="%s"/><label class="full" for="star2" title="2 stars"></label> \
					<input type="radio" id="star1" name="rating" value="1" data-api="%s" checked/><label class="full" for="star1" title="1 star"></label>\
					</div>'	% (
						
					route.get_api_rate_url(5),
					route.get_api_rate_url(4),
					route.get_api_rate_url(3),
					route.get_api_rate_url(2),
					route.get_api_rate_url(1),	

					))

			elif user_rating == 2:
				
				return mark_safe('<div data-api="#" class="rating" id="star-rating">Your rating: \
					<input type="radio" id="star5" name="rating" value="5" data-api="%s"/><label class="full" for="star5" title="5 stars"></label> \
					<input type="radio" id="star4" name="rating" value="4" data-api="%s"/><label class="full" for="star4" title="4 stars"></label> \
					<input type="radio" id="star3" name="rating" value="3" data-api="%s"/><label class="full" for="star3" title="3 stars"></label> \
					<input type="radio" id="star2" name="rating" value="2" data-api="%s" checked/><label class="full" for="star2" title="2 stars"></label> \
					<input type="radio" id="star1" name="rating" value="1" data-api="%s"/><label class="full" for="star1" title="1 star"></label>\
					</div>'	% (
						
					route.get_api_rate_url(5),
					route.get_api_rate_url(4),
					route.get_api_rate_url(3),
					route.get_api_rate_url(2),
					route.get_api_rate_url(1),	

					))

			elif user_rating == 3:
				
				return mark_safe('<div data-api="#" class="rating" id="star-rating">Your rating: \
					<input type="radio" id="star5" name="rating" value="5" data-api="%s"/><label class="full" for="star5" title="5 stars"></label> \
					<input type="radio" id="star4" name="rating" value="4" data-api="%s"/><label class="full" for="star4" title="4 stars"></label> \
					<input type="radio" id="star3" name="rating" value="3" data-api="%s" checked/><label class="full" for="star3" title="3 stars"></label> \
					<input type="radio" id="star2" name="rating" value="2" data-api="%s"/><label class="full" for="star2" title="2 stars"></label> \
					<input type="radio" id="star1" name="rating" value="1" data-api="%s"/><label class="full" for="star1" title="1 star"></label>\
					</div>'	% (
						
					route.get_api_rate_url(5),
					route.get_api_rate_url(4),
					route.get_api_rate_url(3),
					route.get_api_rate_url(2),
					route.get_api_rate_url(1),	

					))

			elif user_rating == 4:

				return mark_safe('<div data-api="#" class="rating" id="star-rating">Your rating: \
					<input type="radio" id="star5" name="rating" value="5" data-api="%s"/><label class="full" for="star5" title="5 stars"></label> \
					<input type="radio" id="star4" name="rating" value="4" data-api="%s" checked/><label class="full" for="star4" title="4 stars"></label> \
					<input type="radio" id="star3" name="rating" value="3" data-api="%s"/><label class="full" for="star3" title="3 stars"></label> \
					<input type="radio" id="star2" name="rating" value="2" data-api="%s"/><label class="full" for="star2" title="2 stars"></label> \
					<input type="radio" id="star1" name="rating" value="1" data-api="%s"/><label class="full" for="star1" title="1 star"></label>\
					</div>'	% (
						
					route.get_api_rate_url(5),
					route.get_api_rate_url(4),
					route.get_api_rate_url(3),
					route.get_api_rate_url(2),
					route.get_api_rate_url(1),	

					))

			elif user_rating == 5:

				return mark_safe('<div data-api="#" class="rating" id="star-rating">Your rating: \
					<input type="radio" id="star5" name="rating" value="5" data-api="%s" checked/><label class="full" for="star5" title="5 stars"></label> \
					<input type="radio" id="star4" name="rating" value="4" data-api="%s"/><label class="full" for="star4" title="4 stars"></label> \
					<input type="radio" id="star3" name="rating" value="3" data-api="%s"/><label class="full" for="star3" title="3 stars"></label> \
					<input type="radio" id="star2" name="rating" value="2" data-api="%s"/><label class="full" for="star2" title="2 stars"></label> \
					<input type="radio" id="star1" name="rating" value="1" data-api="%s"/><label class="full" for="star1" title="1 star"></label>\
					</div>'	% (

					route.get_api_rate_url(5),
					route.get_api_rate_url(4),
					route.get_api_rate_url(3),
					route.get_api_rate_url(2),
					route.get_api_rate_url(1),	

					))
		

			else:
				return "ERROR"

	else:
		return mark_safe('<small>Log in to rate!</small>')

@register.filter(name='get_rating_count')
def get_rating_count(route, user):
	return route.rating_set.filter(user=user).count()







