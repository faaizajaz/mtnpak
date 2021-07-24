from django.shortcuts import render, redirect
from .models import Route
from django.views import generic
from django.shortcuts import get_object_or_404
from routes.forms import AddAscentToRouteForm
from django.contrib.auth.decorators import login_required
from pitches.forms import *
from utils.conversions import convert_units
from ratings.models import Rating
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from comments.forms import AddCommentForm
from django.contrib.auth.decorators import permission_required


#this is the view for a routes home page.
# I have not created a tmeplate for this.
class RoutesHome(generic.ListView):
    template_name = 'routes/routes-home.html'
    model = Route

    def get_queryset(self):
        return Route.objects.all()

#this is the view you get when you click on a route.
class RouteView(generic.DetailView):
    template_name = 'routes/route-view.html'
    model = Route

    def get_object(self):
        #get current route and store in variable
        current_route = get_object_or_404(Route, pk=self.kwargs['route_id'])
        return current_route


    # This is a CBV built in method that you can override to add additional
    # context so, in this case I'm adding the commentform()
    def get_context_data(self, **kwargs):
        context = super(RouteView, self).get_context_data(**kwargs)
        context['comment_form'] = AddCommentForm()
        return context


# this is the comment api for routes. Comments are posted to this
# API endpoint.
class RouteCommentAPI(APIView):
    authentication
    _classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, route_id=None, format=None):
        #print(request.data['csrfmiddlewaretoken'])
        route = get_object_or_404(Route, pk=route_id)
        user = self.request.user
        body = request.data['body']
        route.comments.create(body=body, user=user)
        return Response("success")

class RouteRatingAPI(APIView):
    #make sure authenticated and permitted for api call
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    #routeid and score = None because otherwise it has unepected keyword arg error
    def get(self, request, format=None, route_id=None, score=None):
        route = get_object_or_404(Route, pk=route_id)
        user = self.request.user
        #make rating 
        rating = Rating(score=score, route=route, user=user)
        #add rating to route.abs
        # add_rating returns an average rating.
        return Response(route.add_rating(user, rating))


@login_required
def AddAscentToRoute(request, **kwargs):
    if request.method == 'POST':
        form = AddAscentToRouteForm(request.POST)
        if form.is_valid():
            #route_id = kwargs['route_id']
            #print(form.save(commit=False).date)
            newascent = form.save(commit=False)
            newascent.climber = request.user
            newascent.route = Route.objects.get(pk=kwargs['route_id'])
            newascent.save()
            
            return redirect('route-view', route_id=kwargs['route_id'])
    else:
        #form = AddAscentForm(initial={'climber': request.user})
        form = AddAscentToRouteForm()
    return render(request, 'routes/addascenttoroute.html', {'form': form})


#WHY IS THIS VIEW HERE? OR RATHER WHY ARE ADD ROUTE/MULTI AND ROUTE CHOICE in crags.views?
@login_required
@permission_required('routes.add_route', login_url="/unauthorized_URL/")
@permission_required('pitches.add_pitch', login_url="/unauthorized_URL/")
def AddPitchMulti(request, **kwargs):
    ##SET SESSION PREFERENCE VARIABLES
    try:
        grade_pref = request.session['grade_pref']
        measurement_pref = request.session['measurement_pref']
    except KeyError:
        grade_pref = 'French'
        measurement_pref = 'meters'

    if request.method == 'POST':
        
        # render the correct form with correct fields depending on user_pref
        if grade_pref == "YDS":
            form = AddPitchFormYDSMulti(request.POST)
        elif grade_pref == "French":
            form = AddPitchFormFrenchMulti(request.POST)
        
        

        if form.is_valid():
            newpitch = form.save(commit=False)
            newpitch.proute = Route.objects.get(pk=kwargs['route_id'])
            
            #Set base unit for the new pitch to pref of user adding it.
            newpitch.base_unit = measurement_pref

            #check if ROUTE base unit is equal to base unit of pitch being added
            if newpitch.proute.base_unit == newpitch.base_unit:
                # if equal, add to route length
                newpitch.proute.length += newpitch.length
                
            else:
                # if not equal, convery current pitch length to ROUTE base unit, then add
                newpitch.proute.length += convert_units(newpitch.base_unit, newpitch.proute.base_unit, newpitch.length)

            newpitch.proute.save()
            newpitch.save()

            # Once route is saved, set grade to the highest grade of its pitch_set
            newpitch.proute.get_highest_grade()
            
            return redirect('route-view', route_id=kwargs['route_id'])
    else:
        if grade_pref == "YDS":
            form = AddPitchFormYDSMulti()
        elif grade_pref == "French":
            form = AddPitchFormFrenchMulti()


    return render(request, 'routes/addpitch.html', {'form': form})




