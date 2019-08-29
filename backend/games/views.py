
#Django REST Framerwork
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView


#Models 
from games.models import Game

#Serializers
from games.serializers import GameSerializer


class GameViewSet(mixins.ListModelMixin,
				viewsets.GenericViewSet):
	"""Game view set"""
	queryset          = Game.objects.all()
	serializers_class = GameSerializer

