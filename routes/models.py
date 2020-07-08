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








