from django.db import models

# Create your models here.
class CD(models.Model):
	band_name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	track_number = models.CharField(max_length=3)
	total_length = models.CharField(max_length=100)
	price = models.CharField(max_length=100)

	def __str__(self):
		return self.band_name