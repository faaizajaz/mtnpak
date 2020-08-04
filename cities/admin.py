from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import City

# Register your models here.
admin.site.register(City, LeafletGeoAdmin)
