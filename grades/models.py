from django.db import models

class Grade(models.Model):
    #ggrade is french grade, need to refactor
    numgrade = models.IntegerField(verbose_name='Integer representation of grades')
    ggrade = models.CharField(max_length=10, verbose_name='French Grade', blank=True)
    ydsgrade = models.CharField(max_length=10, verbose_name='YDS Grade', blank=True)

    def __str__(self):
    	return f'{self.ggrade}'

    def natural_key(self):
    	return self.ydsgrade


    def __unicode__(self):
   		return self.ggrade


