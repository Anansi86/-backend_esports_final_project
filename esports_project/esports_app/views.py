from rest_framework import viewsets
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer, CustomUserSerializer, MatchSerializer
from .models import Match, Player, Team, Hero, Hero_player_matches, Match_score
from .serializers import MatchSerializer, PlayerSerializer, TeamSerializer, HeroSerializer, Hero_player_matchesSerializer, Match_scoreSerializer

class ObtainTokenPairWithColorView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CustomUser(viewsets.ModelViewSet):
#     serializer_class = CustomUserSerializer
#     queryset = CustomUser.objects.all().order_by("username")
    

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all().order_by("created")

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all().order_by("name")

class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all().order_by("player_name")

class HeroViewSet(viewsets.ModelViewSet):
    serializer_class = HeroSerializer
    queryset = Hero.objects.all().order_by("name")

class Hero_player_matchesViewSet(viewsets.ModelViewSet):
    serializer_class = Hero_player_matchesSerializer
    queryset = Hero_player_matches.objects.all().order_by("points")

class Match_scoreViewSet(viewsets.ModelViewSet):
    serializer_class = Match_scoreSerializer
    queryset = Match_score.objects.all().order_by("match_id")