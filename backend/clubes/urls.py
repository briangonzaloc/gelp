# from django.urls import path, include

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

# from .views import games as game_views
from .views import ClubViewSet

router = DefaultRouter()
router.register(r'clubes', ClubViewSet, basename='clubes')
# router.register(
# 	r'clubes/(?P<pk_club>\d+)/games',
# 	game_views.GameViewSet,
# 	basename='games'
# )


# router.register(r'games', game_views.GameViewSet, basename='games')

urlpatterns = [
	url(r'^', include(router.urls)),
]