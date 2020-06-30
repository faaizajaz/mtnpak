from django.db import models

class Grade(models.Model):
    #ggrade is french grade, need to refactor
    ggrade = models.CharField(max_length=10, verbose_name='French Grade', blank=True)
    ydsgrade = models.CharField(max_length=10, verbose_name='YDS Grade', blank=True)
    ausgrade = models.CharField(max_length=10, verbose_name='Ewbanks Grade', blank=True)
    uiaagrade = models.CharField(max_length=10, verbose_name='UIAA Grade', blank=True)
    sagrade = models.CharField(max_length=10, verbose_name='SA Grade', blank=True)
    ukgrade = models.CharField(max_length=10, verbose_name='UK Grade', blank=True)

    def __str__(self):
    	return f'{self.ggrade}'

