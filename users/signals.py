from django.db.models.signals import post_save  # gets triggered after object is saved
from django.contrib.auth.models import User  # User is the object which is saved (sender)
from django.dispatch import receiver
from .models import Profile
from userprefs.models import UserPref


#sent at end of User models save() -> i.e. when User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	#created is a bool from the builtin post_save signal, True if new record created
	if created:
		#create a new Profile using query with the instance (var sent by post_save) as
		#the user attribute for the Profile object
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()


@receiver(post_save, sender=User)
def create_userprefs(sender, instance, created, **kwargs):
	if created:
		UserPref.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_userprefs(sender, instance, **kwargs):
	instance.userpref.save()

