from django.db import models

class Club(models.Model):
	""" CLub model """
	name      = models.CharField(unique=True, max_length=150)
	dim_x     = models.FloatField(help_text="Playing field length")
	dim_y     = models.FloatField(help_text="Playing field width")

	def __str__(self):
		return self.name

	# def get_short_name(self):
	# 	return ''.join(character for character in self.name if character.isupper())

