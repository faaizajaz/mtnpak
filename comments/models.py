from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone



# Create your models here.
# class X FK(Y) : an X can only have one Y 

class Comment(models.Model):

	# Comment metadata
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Comment author")
	created = models.DateTimeField(verbose_name="Created date and time", editable=False, default=timezone.now)
	updated = models.DateTimeField(verbose_name="Edited date and time", default=timezone.now)

	# Comment body
	body = models.TextField()

	# Mandatory stuff for Generic relations
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.IntegerField()
	content_object = GenericForeignKey()

	# Overload save() method to puplated created/updated fields
	def save(self, *args, **kwargs):
		# if comment object doesn't already exist, set created
		if not self.id:
			self.created = timezone.now()
		# otherwise set modified
		self.modified = timezone.now()
		return super(Comment, self).save(*args, **kwargs)

