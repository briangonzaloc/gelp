#Django REST Framerwork
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView


#Models 
from games.models import Club

#Serializers
from games.serializers import ClubSerializer


class ClubViewSet(mixins.ListModelMixin,
				mixins.RetrieveModelMixin,
				viewsets.GenericViewSet):
	"""Game view set"""
	queryset         = Club.objects.all()
	serializer_class = ClubSerializer

