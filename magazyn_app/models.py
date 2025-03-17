from django.db import models

class Produkt(models.Model):
    nazwa = models.CharField(max_length=255)

    def __str__(self):
        return f"nazwa{self.nazwa}"
    
class WariantProduktu(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE, related_name= "wariant")
    rozmiar = models.CharField(max_length=50)
    ilosc = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.produkt.nazwa} - {self.rozmiar}"

class Karton(models.Model):
    kod_kartonu = models.CharField(max_length=50)
    produkty = models.ManyToManyField(WariantProduktu, related_name="kartony")

    def __str__(self):
        return f"Karton{self.kod_kartonu}"

class Sekcja(models.Model):
    nazwa = models.CharField(max_length=50)
    lista_kartonow = models.ManyToManyField(Karton, related_name="sekcje")

    def __str__(self):
        return f"nazwa{self.nazwa}"
    
class Hisotria(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    typ_operacji = models.CharField(max_length=50, choices= [("Dodaj", "Dodanie"), ("Usun", "Usuniecie")])
    ilosc_zmiany = models.IntegerField()

    def __str__(self):
        return f"{self.data} - {self.typ_operacji}{self.ilosc_zmiany} x {self.produkt}"

