from django.shortcuts import render, redirect
from .models import Crag
from django.views import generic
from django.shortcuts import get_object_or_404
from .forms import AddRouteForm, AddCragForm, RouteChoiceForm, AddRouteMultiForm
from pitches.forms import AddPitchForm



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

# replace with class based form view
def AddRoute(request, **kwargs):
	if request.method == 'POST':
		form = AddRouteForm(request.POST)
		form2 = AddPitchForm(request.POST)
		if form.is_valid(): #and form2.is_valid():
			newroute = form.save(commit=False)
			newroute.ropener = request.user
			newroute.rcrag = Crag.objects.get(pk=kwargs['crag_id'])
			newroute.numpitch = 'Singlepitch'
			newroute.save()
			

			newpitch = form2.save(commit=False)
			newpitch.proute = newroute
			newpitch.save()

			return redirect('crag-view', crag_id=kwargs['crag_id'])
	else:
		form = AddRouteForm()
		form2 = AddPitchForm()
	return render(request, 'crags/addroute.html', {'form': form, 'form2':form2})

def AddRouteMulti(request, **kwargs):
	if request.method == 'POST':
		form = AddRouteMultiForm(request.POST)
		if form.is_valid(): #and form2.is_valid():
			newroute = form.save(commit=False)
			newroute.ropener = request.user
			newroute.rcrag = Crag.objects.get(pk=kwargs['crag_id'])
			newroute.numpitch = 'Multipitch'
			newroute.save()
			#return redirect('crag-view', crag_id=kwargs['crag_id'])
			return redirect('route-view', route_id=newroute.id)
	else:
		form = AddRouteMultiForm()
	return render(request, 'crags/addroute.html', {'form': form})


#choose between single and multipitch when adding new route.
def RouteChoice(request, **kwargs):
	if request.method == 'POST':
		form = RouteChoiceForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			choice = cd.get('choice')
			if choice == 'single':
				crag_id=kwargs['crag_id']
				print('single putch')
				return redirect('add-route', crag_id=crag_id)
			elif choice == 'multi':
				crag_id=kwargs['crag_id']
				print('multipitch')
				return redirect('add-route-multi', crag_id=crag_id)
	else:
		form = RouteChoiceForm()
	return render(request, 'crags/routechoice.html', {'form': form})



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
