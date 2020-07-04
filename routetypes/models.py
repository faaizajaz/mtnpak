from django.db import models


class RouteType(models.Model):
	#properties of trad route go here
	route_type = models.CharField(max_length=50, verbose_name='Type of route')

	def __str__(self):
		return f'{self.route_type}'





