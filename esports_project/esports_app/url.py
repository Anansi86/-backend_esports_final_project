from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView, CustomUserCreate
from esports_app import views
from esports_app.views import MatchViewSet, PlayerViewSet, TeamViewSet, HeroViewSet, Hero_player_matchesViewSet, Match_score #CustomUser

router = routers.DefaultRouter()
router.register(r'Match', views.MatchViewSet)
router.register(r'Team', views.TeamViewSet)
router.register(r'Player', views.PlayerViewSet)
router.register(r'Hero', views.HeroViewSet)
router.register(r'Hero_player_matches', Hero_player_matchesViewSet)
router.register(r'Match_score', views.Match_scoreViewSet)
#router.register(r'CustomUser', views.CustomUserViewSet)

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('user/login/', ObtainTokenPairWithColorView.as_view(), name='token_create'),  
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]