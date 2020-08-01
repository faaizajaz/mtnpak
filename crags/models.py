from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PointField
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment
from django_quill.fields import QuillField



class Crag(models.Model):
    cname = models.CharField(max_length=500, verbose_name='Name')
    cdescription = QuillField(max_length=50000, verbose_name='Crag description')
    cauthor = models.ForeignKey(  # Many crags can have one author
        User, on_delete=models.PROTECT, verbose_name='Page author')
    location = PointField()

    comments = GenericRelation(Comment, related_query_name='crag-comments')



    def __str__(self):
        return self.cname

    def get_absolute_url(self):
        from django.urls import reverse
        # return the string URL for route-view (in urls.py) using self.id as arg
        return reverse('crag-view', args=[str(self.id)])

    def count_routes(self):
    	return self.route_set.all().count()

