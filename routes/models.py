from django.db import models
from crags.models import Crag
from routetypes.models import *







class Route(models.Model):
    rname = models.CharField(max_length=500, verbose_name='Route Name')
    rdescription = models.TextField(verbose_name='Route Description')
    ropener = models.CharField(max_length=500, verbose_name='Route Opener')
    rcrag = models.ForeignKey(Crag, on_delete=models.CASCADE, verbose_name='Crag')
    
    # equal to pitch length if one pitch, otherwise sum of pitch length
    rlength = models.IntegerField(verbose_name='Route Length', default=0)
    # this should be set once and never changed.
    rbase_unit = models.CharField(max_length=50, verbose_name='R Base_unit')

    rtype = models.ForeignKey(RouteType, on_delete=models.SET_NULL, null=True)

    numpitch = models.CharField(max_length=500, verbose_name='Single or Multi')


    # When I need to list all routes, can do:
    # routes = Route.objects.select_subclasses(TradRoute)


    def __str__(self):
        return self.rname


#class TradRoute(Route):

#	def __str__(self):
#		return self.rname
	#specific route properties for trad routes



#class SportRoute(Route):
	#specific route properties for sport routes


#class MixedRoute(Route):
	#specific properties for sport routes





