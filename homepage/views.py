from django.shortcuts import render
from routes.models import Route
from crags.models import Crag



def HomePage(request):

    top_routes = Route.objects.all().order_by('-avg_rating')[:10]
    crag_list = []


    for crag in Crag.objects.all():
    	crag_list.append({
    		'name': crag.cname,
    		'crag_id': crag.id,
    		'url' : crag.get_absolute_url(),
    		'route_count': crag.count_routes(),
    		'lat': crag.location['coordinates'][1],
    		'lon': crag.location['coordinates'][0]
    		})
   

    context = {'top_routes': top_routes, 'crag_list': crag_list}


    return render(request, 'homepage/homepage.html', context)
