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

    avg_rating = models.IntegerField(verbose_name='Average rating', default=0)


    def __str__(self):
        return self.rname







