from django.urls import path
from . import views
from userprefs.views import UpdateUserPrefs

urlpatterns = [
    path('<username>', views.UserProfile.as_view(), name='profile'),
    path('<username>/edit', views.EditProfile, name='edit-profile'),
    path('<username>/editprefs', UpdateUserPrefs, name='edit-prefs')
]
