from django.shortcuts import render
from .forms import RouteFinderFormYDS, RouteFinderFormFrench
from routes.models import Route
from django.db.models import Q

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
			# save form data and create a query object
			data = form.cleaned_data
			query = Q()

			# if the user has selected a grade, add it to the query
			if data.get('max_grade'):
				query.add(Q(grade__lte=data.get('max_grade')), Q.AND)

			# if the user has selected a route type, add it to the query
			if data.get('route_type') != 'Any':
				query.add(Q(rtype=data.get('route_type')), Q.AND)

			# if the user has selected a city, add it to the query
			if data.get('city'):
				query.add(Q(rcrag__city=data.get('city')), Q.AND)

			# if the user has selected a TR preference, build OR (|) query and connect
			# to previous with AND
			if data.get('toprope') != 'Any':
				query.add(Q(rcrag__toprope='Some routes') | Q(rcrag__toprope='All routes'), Q.AND)

			# filter route objects with the query
			routes = Route.objects.filter(query).order_by('rcrag')
			

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