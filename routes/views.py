from django.shortcuts import render, redirect
from .models import Route
from django.views import generic
from django.shortcuts import get_object_or_404
from routes.forms import AddAscentToRouteForm
from django.contrib.auth.decorators import login_required
from pitches.forms import *
from utils.conversions import convert_units
from ratings.models import Rating



#this is the view for a routes home page.
class RoutesHome(generic.ListView):
	template_name = 'routes/routes-home.html'
	model = Route

	def get_queryset(self):
		return Route.objects.all()

#this is the view you get when you click on a route.
class RouteView(generic.DetailView):
	template_name = 'routes/route-view.html'
	model = Route

	def get_object(self):
		#get current route and store in variable
		current_route = get_object_or_404(Route, pk=self.kwargs['route_id'])
		return current_route

#create view to add rating to route
class RouteRatingRedirect(generic.RedirectView):
	#override redirect url of this gneeric.RedirectView
	def get_redirect_url(self, **kwargs):
		# save pk of current route
		route_id = self.kwargs['route_id']
		#get the route object using route_id
		obj = get_object_or_404(Route, pk=route_id)
		# do a reverse lookup of the URL of the original route so we can redirect after rating		
		route_url = obj.get_absolute_url()
		# set the user to current user
		user = self.request.user
		# create a rating object with the score, current route, and current user
		rating = Rating(score=5, route=obj, user=user)
		print("made a raring from route rating")

		#save the rating and add it to the Route's ratings
		if user.is_authenticated:
			##### do something like #####
			# if user in obj.rating_set or something
			rating.save()
			obj.rating_set.add(rating)
		#redirect to the original route's page
		return route_url

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

#Making an API view
class RouteRatingRedirectAPI1(APIView):

	#I guess django rest needs to do this
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	# i think route_id=None otherwise it saus get got unexpected keyword arg
	def get(self, request, format=None, route_id=None):
		#get the route object using route_id
		route = get_object_or_404(Route, pk=route_id)
		# set the user to current user
		user = self.request.user
		# create a rating object with the score, current route, and current user
		rating = Rating(score=1.0, route=route, user=user)
		print("made a rating from API 1")

		#save the rating and add it to the Route's ratings
		if user.is_authenticated:
			##### do something like #####
			# if user in obj.rating_set or something, then obj.rating_set.remove()
			# and then save the new rating. This allows users to re-rate.
			if user.username != 'faaiz': #God mode	
				existing_ratings = route.rating_set.filter(user=user).count()
				if existing_ratings == 1:
					route.rating_set.get(user=user).delete()
				elif existing_ratings > 1:
					print("Must be in God mode.")
					#return a response
			#Save the rating object
			rating.save()
			#add the rating object to the route's rating set
			route.rating_set.add(rating)
			#get total number of ratings
			n = route.rating_set.count()
			#create variable to store total of all ratings
			running_total = 0
			#Calculate average rating
			for i in route.rating_set.all():
				running_total += i.score
			if n > 0:
				route.avg_rating = running_total / n
				route.save()
			else:
				route.avg_rating = 0.0

			#percent_rating = round(route.avg_rating/5)
			data = route.avg_rating
		return Response(data)

class RouteRatingRedirectAPI2(APIView):

	#I guess django rest needs to do this
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	# i think route_id=None otherwise it saus get got unexpected keyword arg
	def get(self, request, format=None, route_id=None):
		#get the route object using route_id
		route = get_object_or_404(Route, pk=route_id)
		# set the user to current user
		user = self.request.user
		# create a rating object with the score, current route, and current user
		rating = Rating(score=2.0, route=route, user=user)
		print("made a rating from API 2")

		#save the rating and add it to the Route's ratings
		if user.is_authenticated:
			##### do something like #####
			# if user in obj.rating_set or something, then obj.rating_set.remove()
			# and then save the new rating. This allows users to re-rate.
			if user.username != 'faaiz': #God mode	
				existing_ratings = route.rating_set.filter(user=user).count()
				if existing_ratings == 1:
					route.rating_set.get(user=user).delete()
				elif existing_ratings > 1:
					print("Must be in God mode.")
					#return a response
			#Save the rating object
			rating.save()
			#add the rating object to the route's rating set
			route.rating_set.add(rating)
			#get total number of ratings
			n = route.rating_set.count()
			#create variable to store total of all ratings
			running_total = 0
			#Calculate average rating
			for i in route.rating_set.all():
				running_total += i.score
			if n > 0:
				route.avg_rating = running_total / n
				route.save()
			else:
				route.avg_rating = 0.0

			data = route.avg_rating
		return Response(data)

class RouteRatingRedirectAPI3(APIView):

	#I guess django rest needs to do this
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	# i think route_id=None otherwise it saus get got unexpected keyword arg
	def get(self, request, format=None, route_id=None):
		#get the route object using route_id
		route = get_object_or_404(Route, pk=route_id)
		# set the user to current user
		user = self.request.user
		# create a rating object with the score, current route, and current user
		rating = Rating(score=3.0, route=route, user=user)
		print("made a rating from API 3")

		#save the rating and add it to the Route's ratings
		if user.is_authenticated:
			##### do something like #####
			# if user in obj.rating_set or something, then obj.rating_set.remove()
			# and then save the new rating. This allows users to re-rate.
			if user.username != 'faaiz': #God mode	
				existing_ratings = route.rating_set.filter(user=user).count()
				if existing_ratings == 1:
					route.rating_set.get(user=user).delete()
				elif existing_ratings > 1:
					print("Must be in God mode.")
					#return a response
			#Save the rating object
			rating.save()
			#add the rating object to the route's rating set
			route.rating_set.add(rating)
			#get total number of ratings
			n = route.rating_set.count()
			#create variable to store total of all ratings
			running_total = 0
			#Calculate average rating
			for i in route.rating_set.all():
				running_total += i.score
			if n > 0:
				route.avg_rating = running_total / n
				route.save()
			else:
				route.avg_rating = 0.0

			data = route.avg_rating
		return Response(data)

class RouteRatingRedirectAPI4(APIView):

	#I guess django rest needs to do this
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	# i think route_id=None otherwise it saus get got unexpected keyword arg
	def get(self, request, format=None, route_id=None):
		#get the route object using route_id
		route = get_object_or_404(Route, pk=route_id)
		# set the user to current user
		user = self.request.user
		# create a rating object with the score, current route, and current user
		rating = Rating(score=4.0, route=route, user=user)
		print("made a rating from API 4")

		#save the rating and add it to the Route's ratings
		if user.is_authenticated:
			##### do something like #####
			# if user in obj.rating_set or something, then obj.rating_set.remove()
			# and then save the new rating. This allows users to re-rate.
			if user.username != 'faaiz': #God mode	
				existing_ratings = route.rating_set.filter(user=user).count()
				if existing_ratings == 1:
					route.rating_set.get(user=user).delete()
				elif existing_ratings > 1:
					print("Must be in God mode.")
					#return a response
			#Save the rating object
			rating.save()
			#add the rating object to the route's rating set
			route.rating_set.add(rating)
			#get total number of ratings
			n = route.rating_set.count()
			#create variable to store total of all ratings
			running_total = 0
			#Calculate average rating
			for i in route.rating_set.all():
				running_total += i.score
			if n > 0:
				route.avg_rating = running_total / n
				route.save()
			else:
				route.avg_rating = 0.0

			data = route.avg_rating
		return Response(data)

class RouteRatingRedirectAPI5(APIView):

	#I guess django rest needs to do this
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	# i think route_id=None otherwise it saus get got unexpected keyword arg
	def get(self, request, format=None, route_id=None):
		#get the route object using route_id
		route = get_object_or_404(Route, pk=route_id)
		# set the user to current user
		user = self.request.user
		# create a rating object with the score, current route, and current user
		rating = Rating(score=5.0, route=route, user=user)
		print("made a rating from API 5")

		#save the rating and add it to the Route's ratings
		if user.is_authenticated:
			##### do something like #####
			# if user in obj.rating_set or something, then obj.rating_set.remove()
			# and then save the new rating. This allows users to re-rate.
			if user.username != 'faaiz': #God mode	
				existing_ratings = route.rating_set.filter(user=user).count()
				if existing_ratings == 1:
					route.rating_set.get(user=user).delete()
				elif existing_ratings > 1:
					print("Must be in God mode.")
					#return a response
			#Save the rating object
			rating.save()
			#add the rating object to the route's rating set
			route.rating_set.add(rating)
			#get total number of ratings
			n = route.rating_set.count()
			#create variable to store total of all ratings
			running_total = 0
			#Calculate average rating
			for i in route.rating_set.all():
				running_total += i.score
			if n > 0:
				route.avg_rating = running_total / n
				route.save()
			else:
				route.avg_rating = 0.0

			data = route.avg_rating
		return Response(data)


@login_required
def AddAscentToRoute(request, **kwargs):
	if request.method == 'POST':
		form = AddAscentToRouteForm(request.POST)
		if form.is_valid():
			#route_id = kwargs['route_id']
			#print(form.save(commit=False).date)
			newascent = form.save(commit=False)
			newascent.climber = request.user
			newascent.route = Route.objects.get(pk=kwargs['route_id'])
			newascent.save()
			
			return redirect('route-view', route_id=kwargs['route_id'])
	else:
		#form = AddAscentForm(initial={'climber': request.user})
		form = AddAscentToRouteForm()
	return render(request, 'routes/addascenttoroute.html', {'form': form})


#WHY IS THIS VIEW HERE? OR RATHER WHY ARE ADD ROUTE/MULTI AND ROUTE CHOICE in crags.views?
@login_required
def AddPitchMulti(request, **kwargs):
	##SET SESSION PREFERENCE VARIABLES
	try:
		grade_pref = request.session['grade_pref']
		measurement_pref = request.session['measurement_pref']
	except KeyError:
		grade_pref = 'French'
		measurement_pref = 'meters'

	if request.method == 'POST':
		
		# render the correct form with correct fields depending on user_pref
		if grade_pref == "YDS":
			form = AddPitchFormYDSMulti(request.POST)
		elif grade_pref == "French":
			form = AddPitchFormFrenchMulti(request.POST)
		elif grade_pref == "Aus":
			form = AddPitchFormAusMulti(request.POST)
		elif grade_pref == "UIAA":
			form = AddPitchFormUIAAMulti(request.POST)
		elif grade_pref == "SA":
			form = AddPitchFormSAMulti(request.POST)
		elif grade_pref == "UK":
			form = AddPitchFormUKMulti(request.POST)
		

		if form.is_valid():
			newpitch = form.save(commit=False)
			newpitch.proute = Route.objects.get(pk=kwargs['route_id'])
			
			#Set base unit for the new pitch to pref of user adding it.
			newpitch.base_unit = measurement_pref

			#check if ROUTE base unit is equal to base unit of pitch being added
			if newpitch.proute.base_unit == newpitch.base_unit:
				# if equal, add to route length
				newpitch.proute.length += newpitch.length
				newpitch.proute.save()
			else:
				# if not equal, convery current pitch length to ROUTE base unit, then add
				newpitch.proute.length += convert_units(newpitch.base_unit, newpitch.proute.base_unit, newpitch.length)
				newpitch.proute.save()

			newpitch.save()
			return redirect('route-view', route_id=kwargs['route_id'])
	else:
		if grade_pref == "YDS":
			form = AddPitchFormYDSMulti()
		elif grade_pref == "French":
			form = AddPitchFormFrenchMulti()
		elif grade_pref == "Aus":
			form = AddPitchFormAusMulti()
		elif grade_pref == "UIAA":
			form = AddPitchFormUIAAMulti()
		elif grade_pref == "SA":
			form = AddPitchFormSAMulti()
		elif grade_pref == "UK":
			form = AddPitchFormUKMulti()

	return render(request, 'routes/addpitch.html', {'form': form})




