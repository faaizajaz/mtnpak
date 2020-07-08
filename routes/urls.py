from django.urls import path
from .import views



urlpatterns = [
	path('', views.RoutesHome.as_view(), name='routes-home'),
	path('<route_id>/', views.RouteView.as_view(), name='route-view'),
	path('<route_id>/rateroute/', views.RouteRatingRedirect.as_view(), name='rate-route'),
	path('api/<route_id>/raterouteapi1/', views.RouteRatingRedirectAPI1.as_view(), name='rate-route-api-1'),
	path('api/<route_id>/raterouteapi2/', views.RouteRatingRedirectAPI2.as_view(), name='rate-route-api-2'),
	path('api/<route_id>/raterouteapi3/', views.RouteRatingRedirectAPI3.as_view(), name='rate-route-api-3'),
	path('api/<route_id>/raterouteapi4/', views.RouteRatingRedirectAPI4.as_view(), name='rate-route-api-4'),
	path('api/<route_id>/raterouteapi5/', views.RouteRatingRedirectAPI5.as_view(), name='rate-route-api-5'),
	path('<route_id>/addascent/', views.AddAscentToRoute, name='add-ascent-to-route'),
	path('<route_id>/addpitchmulti/', views.AddPitchMulti, name='add-pitch-multi'),
]