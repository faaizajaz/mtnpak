from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PointField




class Crag(models.Model):
    cname = models.CharField(max_length=500, verbose_name='Name')
    cdescription = models.TextField(verbose_name='Crag description')
    cauthor = models.ForeignKey(  # Many crags can have one author
        User, on_delete=models.PROTECT, verbose_name='Page author')
    location = PointField()



    def __str__(self):
        return self.cname

