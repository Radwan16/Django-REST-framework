from django.db import models
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


