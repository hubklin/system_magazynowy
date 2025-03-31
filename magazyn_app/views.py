from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from . models import Produkt, WariantProduktu, Karton, Sekcja, Hisotria


def home(request):
    return render(request, 'magazyn_app/index.html')

def lista_produktow(request):
    produkty = Produkt.objects.all()
    return render(request, "magazyn_app/lista_produktow.html", {"produkty": produkty})

def info_produkt(request, produkt_id):
    Produkt = get_object_or_404(Produkt, produkt_id)
    warianty = Produkt.warianty.all()

    return render(request, "produkty/szczegoly_produktow.html", {"produkty": Produkt, "warianty": warianty})

