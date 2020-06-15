from django.shortcuts import render, redirect
from .models import Crag
from django.views import generic
from django.shortcuts import get_object_or_404
from .forms import AddRouteForm, AddCragForm


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
		if form.is_valid():
			newroute = form.save(commit=False)
			newroute.ropener = request.user
			newroute.rcrag = Crag.objects.get(pk=kwargs['crag_id'])
			newroute.save()

			return redirect('crag-view', crag_id=kwargs['crag_id'])
	else:
		form = AddRouteForm()
	return render(request, 'crags/addroute.html', {'form': form})


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
