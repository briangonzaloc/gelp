from django.db import models

class Game(models.Model):

	local_club = models.ForeignKey(
		'games.Club', 
		null=True,
		on_delete=models.SET_NULL, 
		related_name='local_club'
	)
	visiting_club = models.ForeignKey(
		'games.Club', 
		null=True,
		on_delete=models.SET_NULL, 
		related_name='visiting_club'
	)
	actions = models.ManyToManyField('games.Action')

	local_goals    = models.PositiveSmallIntegerField(default=0)
	visiting_goals = models.PositiveSmallIntegerField(default=0)
	datetime       = models.DateTimeField(null=True)


	#Stadium