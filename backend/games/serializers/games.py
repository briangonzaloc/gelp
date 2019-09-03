from rest_framework import serializers

#Models
from games.models import Game

#serializers
# from games.serializers import ClubSerializer

class GameSerializer(serializers.ModelSerializer):
	""" Game Serializer """

	local_club    = serializers.StringRelatedField()
	visiting_club = serializers.StringRelatedField()

	class Meta:
		model   = Game
		exclude = ('actions',)