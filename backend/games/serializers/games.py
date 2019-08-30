from rest_framework import serializers

#Models
from games.models import Game

class GameSerializer(serializers.ModelSerializer):
	""" Game Serializer """

	class Meta:
		model   = Game
		exclude = ('actions',)