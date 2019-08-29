from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import GameViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet, basename='games')

games_urls = [
	path('', include(router.urls)),
]