from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser, Match, Player, Team, Hero, Hero_player_matches, Match_score

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
    
        return token

class Match_scoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match_score
        fields = "__all__"

class CustomUserSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name' )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class MatchSerializer(serializers.ModelSerializer):
    team1 = TeamSerializer()
    team2 = TeamSerializer()
    scores = Match_scoreSerializer(many=True)
    class Meta:
            model = Match
            fields = "__all__"


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"

class Hero_player_matchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero_player_matches
        fields = "__all__"

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Player
#         fields = "__all__"