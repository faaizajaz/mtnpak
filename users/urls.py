from django.urls import path
from . import views


urlpatterns = [
    path('<username>', views.UserProfile.as_view(), name='profile'),
    path('<username>/edit', views.EditProfile, name='edit-profile'),
    path('<username>/editprefs', views.UpdateUserPrefs, name='edit-prefs')
]
