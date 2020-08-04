from django.shortcuts import render
from .forms import RouteFinderFormYDS, RouteFinderFormFrench
from routes.models import Route

# Create your views here.
def RouteFinderView(request):
	# check for user grade preference. Use "get()" to avoid KeyError
	grade_pref = request.session.get('grade_pref')

	if request.method == 'POST':
		# if user grade preference exists, check and create appropriate form
		if grade_pref:
			if grade_pref == 'YDS':
				form = RouteFinderFormYDS(request.POST)
			elif grade_pref == 'French':
				form = RouteFinderFormFrench(request.POST)
		# otherwise if no grade pref, use French as default
		else:
			form = RouteFinderFormFrench(request.POST)

		# if form is valid, run a query on Route objects using form data
		if form.is_valid():
			routes = Route.objects.filter(
				# grades less than or equal to form grade
				grade__lte=form.cleaned_data.get('max_grade'),
				rtype=form.cleaned_data.get('route_type')
			)
			# return the query results to the results template
			return render(request, 'routefinder/results.html', {'routes': routes})

	# if no data posted, create empty form.		
	else:
		if grade_pref:
			if grade_pref == 'YDS':
				form = RouteFinderFormYDS()
			elif grade_pref == 'French':
				form = RouteFinderFormFrench()
		else:
			form = RouteFinderFormFrench()
	# render the form to a different template than the results
	return render(request, 'routefinder/finder.html', {'form': form})