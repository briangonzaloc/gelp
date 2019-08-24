from rest_framework import viewsets
from django.contrib.auth.models import User
from games.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
	print('aaaaaaaaaaaaaaaaa')
	queryset = User.objects.all()
	serializer_class = UserSerializer