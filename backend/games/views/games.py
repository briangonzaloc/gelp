#Django REST Framerwork
from rest_framework import mixins, viewsets, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.db.models import Q, Count

#Models 
from games.models import Game
from clubes.models import Club

#Serializers
from games.serializers import GameSerializer, GameDetailsSerializer


class GameViewSet(mixins.ListModelMixin,
				mixins.RetrieveModelMixin,
				viewsets.GenericViewSet):
	"""Game view set"""

	serializer_class = GameSerializer

	def dispatch(self, request, *args, **kwargs):
		#Verify that the club exists
		self.club = get_object_or_404(Club, pk=kwargs['pk_club'])
		return super(GameViewSet, self).dispatch(request, *args, **kwargs)


	def get_queryset(self):
		return Game.objects.filter(Q(visiting_club=self.club)| Q(local_club=self.club))

class GameDetailViewSet(
					mixins.RetrieveModelMixin,
					viewsets.GenericViewSet):

	serializer_class = GameDetailsSerializer
	queryset = Game.objects.all()

	# @action(detail=True, methods=['get'])
	# def statistics(self, request, *args, **kwargs):
	# 	game = self.get_object()
	# 	data = GameDetailsSerializer(game).data
	# 	# import pdb; pdb.set_trace()
	# 	return Response(data, status=status.HTTP_200_OK)