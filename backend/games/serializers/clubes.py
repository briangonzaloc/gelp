from rest_framework import serializers

#Models
from games.models import Club

class ClubSerializer(serializers.ModelSerializer):
	""" Game Serializer """

	class Meta:
		model  = Club
		fields = '__all__'