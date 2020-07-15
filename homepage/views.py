from django.shortcuts import render
from routes.models import Route


def HomePage(request):
    # return HttpResponse('<h1>MTNPAK home page')

    top_routes = Route.objects.all().order_by('-avg_rating')[:10]

    context = {'top_routes': top_routes}


    return render(request, 'homepage/homepage.html', context)
