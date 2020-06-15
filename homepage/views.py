from django.shortcuts import render


def HomePage(request):
    # return HttpResponse('<h1>MTNPAK home page')
    return render(request, 'homepage/homepage.html')
