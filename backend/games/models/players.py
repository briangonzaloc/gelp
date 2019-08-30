from django.db import models

class Player(models.Model):
	
	name     = models.CharField(max_length=200)
	birthday = models.DateField(null=True)
	weight   = models.FloatField(null=True) 
	height   = models.FloatField(null=True)

	def __str__(self):
		return self.name

