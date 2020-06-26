from django.db import models

class Grade(models.Model):
    ggrade = models.CharField(max_length=500, verbose_name='Grade')

    def __str__(self):
    	return f'{self.ggrade}'

