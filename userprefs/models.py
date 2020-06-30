from django.db import models
from django.contrib.auth.models import User

class UserPref(models.Model):
	user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

	grade_pref = models.CharField(max_length=100, verbose_name='Grading system user preference')
	measurement_pref = models.CharField(max_length=100, verbose_name='Measurement system preferece')

	def __str__(self):
		return self.user.first_name