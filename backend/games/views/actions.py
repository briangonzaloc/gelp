from rest_framework import mixins, viewsets, status, serializers
from django.db.models import Count
from rest_framework.generics import get_object_or_404


#Models 
from games.models import Game, Action

#serializers
from games.serializers import ActionDetailsSerializer

class ActionViewSet(viewsets.GenericViewSet,
						mixins.ListModelMixin):

	serializer_class = ActionDetailsSerializer

	def dispatch(self, request, *args, **kwargs):
		#Verify that the club exists
		self.game = get_object_or_404(Game, pk=kwargs['pk_game'])
		return super(ActionViewSet, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		# return Action.objects.filter(game=self.game).annotate(num_action=Count('name'))
		return Action.objects.filter(
			game=self.game,
			club__isnull=False
		).values('name', 'club').annotate(num_action=Count('name'))

