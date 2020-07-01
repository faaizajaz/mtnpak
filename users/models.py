from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from model_utils import Choices

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pictures')

	def __str__(self):
		return f'{self.user.username} Profile'

#OVERRIDE save method to change image size upon submission
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

class UserPref(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	GRADE_PREF = Choices('French', 'YDS', 'Aus', 'UIAA', 'SA', 'UK')
	MEASUREMENT_PREF = Choices('Meters', 'Feet')

	grade_pref = models.CharField(
		choices=GRADE_PREF,
		default=GRADE_PREF.French,
		verbose_name='Grading system user preference',
		max_length=20
		)

	measurement_pref = models.CharField(
		choices=MEASUREMENT_PREF,
		default=MEASUREMENT_PREF.Meters,
		verbose_name='Measurement system preference',
		max_length=20
		)

	def __str__(self):
		return self.user.first_name