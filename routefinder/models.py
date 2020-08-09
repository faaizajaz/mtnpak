from django.db import models
from django.contrib.auth.models import User
from grades.models import Grade
from cities.models import City
#rom djgeojson.fields import PointField

class RoutefinderQuery(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner of query")
	max_grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name="Maximum grade")
	city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Query city')
	route_type = models.CharField(max_length=100, verbose_name='Type of route')
	toprope = models.CharField(max_length=100, verbose_name='Top rope access')
	#location = PointField()

	def __str__(self):
		return self.user

