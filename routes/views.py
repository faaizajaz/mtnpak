from django.shortcuts import render, redirect
from .models import Route
from django.views import generic
from django.shortcuts import get_object_or_404
from routes.forms import AddAscentToRouteForm
from django.contrib.auth.decorators import login_required
from pitches.forms import *
from utils.conversions import convert_units



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




