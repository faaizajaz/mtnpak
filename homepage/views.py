from django.shortcuts import render
from routes.models import Route
from crags.models import Crag



def HomePage(request):
    # Get a list of top 10 routes
    top_routes = Route.objects.all().order_by('-avg_rating')[:10]
    
    #get a list of all crags with coordinates for the map
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
    
    # get the user IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print('x_forwarded_for')
        user_ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        print('HTTP_X_REAL_IP')
        user_ip = request.META.get('HTTP_X_REAL_IP')
    else:
        print('REMOTE_ADDR')
        user_ip = request.META.get('REMOTE_ADDR')

    # build the context
    context = {'top_routes': top_routes, 'crag_list': crag_list, 'user_ip': user_ip}


    return render(request, 'homepage/homepage.html', context)
