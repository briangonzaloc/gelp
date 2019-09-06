# from django.urls import path, include

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import games as game_views
from .views import actions as action_views

router = DefaultRouter()
router.register(r'games', game_views.GameDetailViewSet, basename='gamesdetails')
router.register(
	r'clubes/(?P<pk_club>\d+)/games',
	game_views.GameViewSet,
	basename='games'
)
router.register(r'games/(?P<pk_game>\d+)/statistics', action_views.ActionViewSet,  basename='statistics')


# router.register(r'games', game_views.GameViewSet, basename='games')

urlpatterns = [
	url(r'^', include(router.urls)),
]