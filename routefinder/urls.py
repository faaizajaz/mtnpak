from django.urls import path
from . import views

urlpatterns = [

	path('', views.RouteFinderView, name='route-finder'),

]