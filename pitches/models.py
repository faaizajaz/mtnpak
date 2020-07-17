from django.db import models
from grades.models import Grade
from routes.models import Route

class Pitch(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, verbose_name='Pitch Grade', null=True)
    #pdescription is only shown on the 'pitch' template.
    #if a route only has one pitch, their is no link to a pitch template
    pdescription = models.TextField(verbose_name='Pitch Description', blank=True, default="")
    proute = models.ForeignKey(Route, on_delete=models.DO_NOTHING, verbose_name='Route', null=True)
    length = models.FloatField(verbose_name='Pitch Length', default=0)



    base_unit = models.CharField(max_length=50, verbose_name='P Base_unit')
