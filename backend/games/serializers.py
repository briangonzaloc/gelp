from rest_framework import serializers

#Models
from django.contrib.auth.models import User



class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'is_staff']
