from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pictures')

	def __str__(self):
		return f'{self.user.username} Profile'

#OVERRIDE save method
#gets run after model is saved
	def save(self):
		#run parent class save method first
		super().save()
		#open image for this profile
		img = Image.open(self.image.path)
		#resize image if it is too big
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
