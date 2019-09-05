from rest_framework import serializers

#Models
from players.models import Player

class PlayerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Player
		fields = '__all__'


