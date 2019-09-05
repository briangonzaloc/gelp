from rest_framework import serializers

#Models
from games.models import Game
from games.models import Action

#serializers
from clubes.serializers import ClubSerializer
from players.serializers import PlayerSerializer

class ActionSerializer(serializers.ModelSerializer):

	player = PlayerSerializer(read_only=True)
	class Meta:
		model = Action
		fields = '__all__'



class GameSerializer(serializers.ModelSerializer):
	""" Game Serializer """

	local_club   = serializers.StringRelatedField()
	visiting_club = serializers.StringRelatedField()

	class Meta:
		model   = Game
		exclude = ('actions',)


class GameDetailsSerializer(serializers.ModelSerializer):

	actions       = ActionSerializer(many=True)
	local_club    = ClubSerializer(read_only=True)
	visiting_club = ClubSerializer(read_only=True)

	class Meta:
		model   = Game
		fields = '__all__'