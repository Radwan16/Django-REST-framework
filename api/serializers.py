from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Film,ExtraInfo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['czas_trwania','rodzaj']

class FilmSerializer(serializers.ModelSerializer):
    extra_info = ExtraInfoSerializer(many=False)
    class Meta:
        model = Film
        fields = ['id','tytul', 'opis', 'po_premierze','premiera','rok','imdb_rating','extra_info']

