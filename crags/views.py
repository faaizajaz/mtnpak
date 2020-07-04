from django.shortcuts import render, redirect
from .models import Crag
from django.views import generic
from django.shortcuts import get_object_or_404
from .forms import AddRouteForm, AddCragForm, RouteChoiceForm, AddRouteMultiForm
from pitches.forms import *
from django.contrib.auth.decorators import login_required



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
		elif request.session['grade_pref'] == "Aus":
			form2 = AddPitchFormAus(request.POST)
		elif request.session['grade_pref'] == "UIAA":
			form2 = AddPitchFormUIAA(request.POST)
		elif request.session['grade_pref'] == "SA":
			form2 = AddPitchFormSA(request.POST)
		elif request.session['grade_pref'] == "UK":
			form2 = AddPitchFormUK(request.POST)

		if form.is_valid() and form2.is_valid():
			newroute = form.save(commit=False)
			newpitch = form2.save(commit=False)
			newroute.ropener = request.user
			newroute.rcrag = Crag.objects.get(pk=kwargs['crag_id'])

			#numpitch tells the template what to display. could replace with
			#session variable
			newroute.numpitch = 'Singlepitch'
			# create route variable
			newpitch.proute = newroute
			
			# set base unit for both pitch and route (always equal since single pitch)
			newpitch.base_unit = request.session['measurement_pref']
			newroute.base_unit = request.session['measurement_pref']

			newroute.length = newpitch.length
			
			newroute.save()	
			newpitch.save()			

			return redirect('crag-view', crag_id=kwargs['crag_id'])
	else:
		form = AddRouteForm()
		
		if request.session['grade_pref'] == "YDS":
			form2 = AddPitchFormYDS()
		elif request.session['grade_pref'] == "French":
			form2 = AddPitchFormFrench()
		elif request.session['grade_pref'] == "Aus":
			form2 = AddPitchFormAus()
		elif request.session['grade_pref'] == "UIAA":
			form2 = AddPitchFormUIAA()
		elif request.session['grade_pref'] == "SA":
			form2 = AddPitchFormSA()
		elif request.session['grade_pref'] == "UK":
			form2 = AddPitchFormUK()

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

			#probably don't need to do this as rbase_unit is not used at all
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
