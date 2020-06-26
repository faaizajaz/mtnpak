from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #django docs just want us to do this import this way
    def ready(self):
    	import users.signals
