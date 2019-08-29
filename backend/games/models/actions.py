from django.db import models

class Action(models.Model):

	name  = models.CharField(max_length=70)
	start = models.TimeField()
	end   = models.TimeField()
	pos_x = models.FloatField(help_text="Position on length axis", null=True)
	pos_y = models.FloatField(help_text="Postiion on width axis", null=True)

	description = models.CharField(max_length=50)
	player = models.ForeignKey(
		'games.Player',
		null=True,
		on_delete=models.SET_NULL
	)

	club = models.ForeignKey(
		'games.Club',
		null=True,
		on_delete=models.SET_NULL
	)