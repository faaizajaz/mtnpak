from django.db import models


class RouteType(models.Model):
	#properties of trad route go here
	route_type = models.TextField(verbose_name='Gear Advice')

	def __str__(self):
		return f'{self.route_type}'





