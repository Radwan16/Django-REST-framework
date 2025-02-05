from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class ExtraInfo(models.Model):
    RODZAJE= {
        (0,'Nieznane'),
        (1,'Horror'),
        (2,'Sci-fi'),
        (3,'Drama'),
        (4,'Komedia')
    }
    czas_trwania = models.IntegerField()
    rodzaj = models.IntegerField(choices=RODZAJE, default=0)

class Film(models.Model):
    tytul = models.CharField(max_length=32)
    opis = models.TextField(max_length=256)
    po_premierze = models.BooleanField(default=False)
    premiera = models.DateField(null=True, blank=True)
    rok=models.IntegerField(default=2000)
    imdb_rating=models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    extra_info = models.OneToOneField(ExtraInfo,on_delete=models.Case,null=True, blank=True)
    def __str__(self):
        return self.nasza_nazwa()

    def nasza_nazwa(self):
        return self.tytul + "( " +str(self.rok)+ " )"

class Recenzja(models.Model):
    opis = models.TextField(default='')
    gwiazdki = models.IntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='recenzje')

class Aktor (models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film)
