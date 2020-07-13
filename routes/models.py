from django.db import models
from crags.models import Crag
from routetypes.models import *

class Route(models.Model):
    rname = models.CharField(max_length=500, verbose_name='Route Name')
    rdescription = models.TextField(verbose_name='Route Description')
    ropener = models.CharField(max_length=500, verbose_name='Route Opener')
    rcrag = models.ForeignKey(Crag, on_delete=models.CASCADE, null=True, verbose_name='Crag')
    
    # equal to pitch length if one pitch, otherwise sum of pitch length
    length = models.FloatField(verbose_name='Route Length', default=0)
    # this should be set once and never changed.
    base_unit = models.CharField(max_length=50, verbose_name='R Base_unit')

    rtype = models.ForeignKey(RouteType, on_delete=models.SET_NULL, null=True)

    numpitch = models.CharField(max_length=500, verbose_name='Single or Multi')

    avg_rating = models.FloatField(verbose_name='Average rating', default=0)


    def __str__(self):
        return self.rname

    #function to add rating object to route
    def add_rating(self, user, rating):
        if user.is_authenticated:
            #get users eisting ratings for the route
            existing_ratings = self.rating_set.filter(user=user).count()
            #if there is already a rating
            if existing_ratings == 1:
                #delete that rating
                self.rating_set.get(user=user).delete()
            #If more than 1 rating exists, then something is wrong.
            elif existing_ratings > 1:
                print("errormode")

            #save the current rating.
            rating.save()
            self.rating_set.add(rating)
            ratings_count = self.rating_set.count()
            running_total = 0

            for i in self.rating_set.all():
                running_total+= i.score

            if ratings_count > 0 :
                self.avg_rating = running_total / ratings_count
                self.save()
            else:
                self.avg_rating = 0.0

            return self.avg_rating

    # I need this method for route rating    
    def get_absolute_url(self):
        from django.urls import reverse
        # return the string URL for route-view (in urls.py) using self.id as arg
        return reverse('route-view', args=[str(self.id)])

    #Needed for API
    def get_api_rate_url_1(self):
        from django.urls import reverse
        return reverse('rate-route-api-1', args=[str(self.id)])

    def get_api_rate_url_2(self):
        from django.urls import reverse
        return reverse('rate-route-api-2', args=[str(self.id)])

    def get_api_rate_url_3(self):
        from django.urls import reverse
        return reverse('rate-route-api-3', args=[str(self.id)])

    def get_api_rate_url_4(self):
        from django.urls import reverse
        return reverse('rate-route-api-4', args=[str(self.id)])

    def get_api_rate_url_5(self):
        from django.urls import reverse
        return reverse('rate-route-api-5', args=[str(self.id)])












