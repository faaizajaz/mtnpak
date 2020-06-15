from django.urls import path
from . import views

urlpatterns = [
    path('', views.CragsHome.as_view(), name='crags-home'),
    path('addcrag/', views.AddCrag, name='add-crag'),
    path('<crag_id>/addroute/', views.AddRoute, name='add-route'),
    path('<crag_id>/', views.CragView.as_view(), name='crag-view'),

]
