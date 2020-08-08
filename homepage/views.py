from django.shortcuts import render
from routes.models import Route
from crags.models import Crag
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError



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
    
    #get the user IP
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

    #user_ip = [24.9043, 67.0817]

    # build some coordinates for homepage map to set its view
    try:
        gip = GeoIP2()
        user_lat, user_lon = list(gip.lat_lon(user_ip))
        zoom_level = 9
    # If there is no address (e.g. on dev server) set a default map view
    except AddressNotFoundError:
        user_lat, user_lon = [31, 70]
        zoom_level = 4.5



    # build the context
    context = {
        'top_routes': top_routes, 
        'crag_list': crag_list, 
        'user_lat': user_lat,
        'user_lon': user_lon, 
        'zoom_level': zoom_level
    }


    return render(request, 'homepage/homepage.html', context)
