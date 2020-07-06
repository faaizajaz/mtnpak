from django.urls import path
from .import views



urlpatterns = [
	path('', views.RoutesHome.as_view(), name='routes-home'),
	path('<route_id>/', views.RouteView.as_view(), name='route-view'),
	path('<route_id>/rateroute/', views.RouteRatingRedirect.as_view(), name='rate-route'),
	path('api/<route_id>/raterouteapi/', views.RouteRatingRedirectAPI.as_view(), name='rate-route-api'),
	path('<route_id>/addascent/', views.AddAscentToRoute, name='add-ascent-to-route'),
	path('<route_id>/addpitchmulti/', views.AddPitchMulti, name='add-pitch-multi'),
]