from django.urls import path
from . import views

urlpatterns = [
    path('', views.CragsHome.as_view(), name='crags-home'),
    path('addcrag/', views.AddCrag, name='add-crag'),
    path('<crag_id>/addroute/', views.AddRoute, name='add-route'),
    path('<crag_id>/addroutemulti/', views.AddRouteMulti, name='add-route-multi'),
    path('<crag_id>/', views.CragView.as_view(), name='crag-view'),
    path('<crag_id>/routechoice/', views.RouteChoice, name='route-choice'),
    path('api/<crag_id>/', views.CragMapAPIView.as_view(), name='crag-map-api'),
    path('api/<crag_id>/comment/', views.CragCommentAPI.as_view(), name='crag-comment-api'),

]
