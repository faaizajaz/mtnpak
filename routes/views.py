from django.shortcuts import render, redirect
from .models import Route
from django.views import generic
from django.shortcuts import get_object_or_404
from routes.forms import AddAscentToRouteForm



class RoutesHome(generic.ListView):
	template_name = 'routes/routes-home.html'
	model = Route

	def get_queryset(self):
		return Route.objects.all()

class RouteView(generic.DetailView):
	template_name = 'routes/route-view.html'
	model = Route

	def get_object(self):
		return get_object_or_404(Route, pk=self.kwargs['route_id'])


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

