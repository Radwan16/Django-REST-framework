from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from api.serializers import UserSerializer
from .models import Film
from .serializers import FilmSerializer, FilmMiniSerializer
from rest_framework.response import Response
from django.http.response import HttpResponseNotAllowed
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get_queryset(self):
        filmy = Film.objects.all()
        return filmy


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = FilmSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FilmSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # if request.user.is_superuser:
        film = Film.objects.create(tytul=request.data['tytul'],
                                opis=request.data['opis'],
                                qpo_premierze=request.data['po_premierze'])
        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)
        # else:
        #     return HttpResponseNotAllowed('Not allowed')

    def update(self, request, *args, **kwargs):
        film = self.get_object()
        film.tytul = request.data['tytul']
        film.opis = request.data['opis']
        film.po_premierze = request.data['po_premierze']
        film.save()
        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        film = self.get_object()
        film.delete()
        return Response('Film usuniety')

    @action(detail=False, methods=['post'])
    def premiera_wszystkie(self, request, **kwargs):
        filmy = Film.objects.all()
        filmy.update(po_premierze=request.data['po_premierze'])

        serializer = FilmSerializer(filmy, many=True)
        return Response(serializer.data)

