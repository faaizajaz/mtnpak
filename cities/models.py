from django.db import models
from djgeojson.fields import PointField

class City(models.Model):
	name = models.CharField(max_length=500, verbose_name='City name')
	location = PointField()

	def __str__(self):
		return self.name