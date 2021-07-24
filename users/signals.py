from django.db.models.signals import post_save  # gets triggered after object is saved
from django.contrib.auth.models import (
    User,
)  # User is the object which is saved (sender)
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import Profile, UserPref
from django.utils import timezone
import pytz
from django.conf import settings


# sent at end of User models save() -> i.e. when User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # created is a bool from the builtin post_save signal, True if new record created
    if created:
        # create a new Profile using query with the instance (var sent by post_save) as
        # the user attribute for the Profile object
        Profile.objects.create(user=instance)


# save profile if user is saved afain
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


##NOTE: TO save request session vars on update userprefs, need to add to user.views.UpdateUserPrefs

# creating request variables when user logs in
def create_pref_session(sender, user, request, **kwargs):
    request.session['grade_pref'] = user.userpref.grade_pref
    request.session['measurement_pref'] = user.userpref.measurement_pref

    # If a timezone is set, activate that timezone
    if user.userpref.timezone_pref:
        request.session['timezone_pref'] = str(user.userpref.timezone_pref)
        timezone.activate(pytz.timezone(request.session['timezone_pref']))
    # otherwise use the default timezone
    else:
        timezone.activate(pytz.timezone(settings.TIME_ZONE))


# IDK but this done because @receiver(user_logged_in,...) didn;t work
user_logged_in.connect(create_pref_session)


# resets the timezone to default if a user logs out.
def reset_timezone_pref(sender, **kwargs):
    timezone.activate(pytz.timezone(settings.TIME_ZONE))


user_logged_out.connect(reset_timezone_pref)
