from django.db import models
from django.contrib.auth.models import User
from crags.models import Crag
from django.urls import reverse


class Route(models.Model):
    rname = models.CharField(max_length=500, verbose_name='Route Name')
    rdescription = models.TextField(verbose_name='Route Description')
    ropener = models.CharField(max_length=500, verbose_name='Route Opener')
    rcrag = models.ForeignKey(Crag, on_delete=models.CASCADE, verbose_name='Crag')


    def __str__(self):
        return self.rname


