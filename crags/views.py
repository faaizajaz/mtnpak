from django.shortcuts import render, redirect
from .models import Crag
from django.views import generic
from django.shortcuts import get_object_or_404
from .forms import AddRouteForm, AddCragForm, RouteChoiceForm, AddRouteMultiForm
from pitches.forms import *
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response

#from rest_framework import authentication, permissions

class CragsHome(generic.ListView):
	template_name = 'crags/crags-home.html'
	model = Crag

	def get_queryset(self):
		return Crag.objects.all()

class CragView(generic.DetailView):
	template_name = 'crags/crag-view.html'
	model = Crag

	def get_object(self):
		return get_object_or_404(Crag, pk=self.kwargs['crag_id'])


### NEED TO REDO THIS. NOT DRY, COULD ROLL MY OWN SERIALIZER ####
class CragMapAPIView(APIView):
	#authentication_classes = (authentication.SessionAuthentication,)
	#permission_classes = (permissions.IsAuthenticated,)

	def get(self, request, format=None, crag_id=None):
		crag = get_object_or_404(Crag, pk=crag_id)

		## FUCK DJANGO SERIALIZERS. I'M DOING IT MYSELF ##
		json_list = []
		route_dict = {}
		fields_dict = {}		

		try:
			pref = request.session['grade_pref']
			
			if pref == 'YDS':
				for route in crag.route_set.all():
					fields_dict = {
						"name": route.rname,
						"grade": route.grade.ydsgrade
					}

					route_dict = {
						"pk": route.id,
						"fields": fields_dict
					}
					json_list.append(route_dict)

			elif pref == 'French':
				for route in crag.route_set.all():
					fields_dict = {
						"name": route.rname,
						"grade": route.grade.ggrade
					}

					route_dict = {
						"pk": route.id,
						"fields": fields_dict
					}
					json_list.append(route_dict)

		except KeyError:

			for route in crag.route_set.all():
				fields_dict = {
					"name": route.rname,
					"grade": route.grade.ggrade
				}

				route_dict = {
					"pk": route.id,
					"fields": fields_dict
				}
				json_list.append(route_dict)

		return Response(json_list)


#IN AddRoute, a route and pitch form are both created since for single
#the route only had 1 pitch. We create the pitch and route here simultatenous
@login_required
def AddRoute(request, **kwargs):
	if request.method == 'POST':
		form = AddRouteForm(request.POST)

		#Choose view based on user pref		
		if request.session['grade_pref'] == "YDS":
			form2 = AddPitchFormYDS(request.POST)
		elif request.session['grade_pref'] == "French":
			form2 = AddPitchFormFrench(request.POST)


		if form.is_valid() and form2.is_valid():
			newroute = form.save(commit=False)
			newpitch = form2.save(commit=False)
			newroute.ropener = request.user
			newroute.rcrag = Crag.objects.get(pk=kwargs['crag_id'])

			newroute.numpitch = 'Singlepitch'
			# create route variable
			newpitch.proute = newroute
			
			# set base unit for both pitch and route (always equal since single pitch)
			# both are only set once.
			newpitch.base_unit = request.session['measurement_pref']
			newroute.base_unit = request.session['measurement_pref']

			newroute.length = newpitch.length
			newroute.grade = newpitch.grade
			
			newroute.save()	
			newpitch.save()			

			return redirect('crag-view', crag_id=kwargs['crag_id'])
	else:
		form = AddRouteForm()
		
		if request.session['grade_pref'] == "YDS":
			form2 = AddPitchFormYDS()
		elif request.session['grade_pref'] == "French":
			form2 = AddPitchFormFrench()


	return render(request, 'crags/addroute.html', {'form': form, 'form2':form2})

#However when adding a multipitch route, we need to first create a route
#with no grade or length field in the form (because those are per pitch)
@login_required
def AddRouteMulti(request, **kwargs):
	if request.method == 'POST':
		form = AddRouteMultiForm(request.POST)
		if form.is_valid(): #and form2.is_valid():
			newroute = form.save(commit=False)
			newroute.ropener = request.user
			newroute.rcrag = Crag.objects.get(pk=kwargs['crag_id'])
			newroute.numpitch = 'Multipitch'

			# ROUTE base unit is set only once, when route is added.
			newroute.base_unit = request.session['measurement_pref']

			newroute.save()
			#return redirect('crag-view', crag_id=kwargs['crag_id'])
			return redirect('route-view', route_id=newroute.id)
	else:
		form = AddRouteMultiForm()
	return render(request, 'crags/addroute.html', {'form': form})


#choose between single and multipitch when adding new route.
@login_required
def RouteChoice(request, **kwargs):
	if request.method == 'POST':
		form = RouteChoiceForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			choice = cd.get('choice')
			if choice == 'single':
				crag_id=kwargs['crag_id']
				return redirect('add-route', crag_id=crag_id)
			elif choice == 'multi':
				crag_id = kwargs['crag_id']
				return redirect('add-route-multi', crag_id=crag_id)
	else:
		form = RouteChoiceForm()
	return render(request, 'crags/routechoice.html', {'form': form})


@login_required
def AddCrag(request, **kwargs):
	if request.method == 'POST':
		form = AddCragForm(request.POST)
		if form.is_valid():
			newcrag = form.save(commit=False)
			newcrag.cauthor = request.user
			newcrag.save()

			return redirect('crags-home')
	else:
		form = AddCragForm()
	return render(request, 'crags/addcrag.html', {'form': form})
