from django.db import models
from routes.models import Route
from django.contrib.auth.models import User

class Rating(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Rating owner')
	route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='Rating route')

	score = models.IntegerField(verbose_name='Rating score', default=0)

	def __str__(self):
		return f"{self.user} - {self.route} - {self.score}"