from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, filters
from api.serializers import UserSerializer
from .models import Film,Recenzja,Aktor
from .serializers import FilmSerializer, RecenzjaSerializer,AktorSerializer
from rest_framework.response import Response
from django.http.response import HttpResponseNotAllowed
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filterset_fields = ['tytul', 'opis','rok']
    filter_backends = [filters.SearchFilter]
    search_fields = ['tytul', 'opis']

    def get_queryset(self):
        # rok = self.request.query_params.get('rok' , None)
        # id = self.request.query_params.get('id' , None)
        #
        # if id:
        #     film = Film.objects.filter(id=id)
        #     return film
        # else:
        #     if rok:
        #         filmy = Film.objects.filter(rok=rok)
        #     else:
        filmy = Film.objects.all()
        return filmy


    # def list(self, request, *args, **kwargs):
    #     # queryset = self.get_queryset()
    #     tytul = self.request.query_params.get('tytul', None)
    #
    #     # film = Film.objects.filter(tytul__exact=tytul)
    #     # film = Film.objects.filter(tytul__icontains=tytul)
    #     film = Film.objects.filter(premiera__year="2000")
    #     serializer = FilmSerializer(film, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FilmSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # if request.user.is_superuser:
        film = Film.objects.create(tytul=request.data['tytul'],
                                opis=request.data['opis'],
                                po_premierze=request.data['po_premierze'],
                                rok=request.data['rok'])
        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)
        # else:
        #     return HttpResponseNotAllowed('Not allowed')

    def update(self, request, *args, **kwargs):
        film = self.get_object()
        film.tytul = request.data['tytul']
        film.opis = request.data['opis']
        film.po_premierze = request.data['po_premierze']
        film.rok = request.data['rok']
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

class RecenzjaViewSet(viewsets.ModelViewSet):
    queryset = Recenzja.objects.all()
    serializer_class = RecenzjaSerializer

class AktorViewSet(viewsets.ModelViewSet):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer

    @action(detail=True, methods=['post'])
    def dolacz(self, request, **kwargs):
        aktor = self.get_object()
        film = Film.objects.get(id=request.data['film'])
        aktor.filmy.add(film)
        
        serializer = AktorSerializer(filmy, many=False)
        return Response(serializer.data)