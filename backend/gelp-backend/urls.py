from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin


# from games.urls import games_urls
from importer.urls import importer_urls
# from games.views import UserViewSet

# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
	path('admin/', admin.site.urls ),
	# path('api/clubes/', include(games_urls) ),
	path('api/importer/', include(importer_urls)),

	path('api/',include( ('games.urls', 'clubes'), namespace='clubes'))

	# url(r'^', include(router.urls)),
	# url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]