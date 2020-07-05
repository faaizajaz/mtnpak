from django.db import models
from django.contrib.auth.models import User
from routes.models import Route



class Ascent(models.Model):
	route = models.ForeignKey(Route, on_delete=models.CASCADE)
	climber = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(auto_now=False)

	def __str(self):
		return self.route.rcrag.cname 