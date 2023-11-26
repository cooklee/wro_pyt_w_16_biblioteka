from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from polka.models import Person

def index(request):
    return render(request, 'base.html')

def hello_django(request):
    return HttpResponse("Witaj Django")

def napis(request, ilosc):
    s = ""
    for x in range(ilosc):
        s+= "dupa<br>"
    return HttpResponse(s)


def tabliczka(request, a, b):
    a = int(a)
    tab = "<table border=1>"
    for x in range(1, a+1):
        tab += "<tr>"
        for y in range(1, b+1):
            tab += f"<td>{x*y}</td>"
        tab+= "</tr>"
    tab += "</table>"
    return HttpResponse(tab)


def dodaj_osobe(request):
    if request.method == "GET":
        response = render(request, 'dodaj_osobe.html')
        return response
    else:
        imie = request.POST['first_name']
        nazwisko = request.POST['last_name']
        p = Person (first_name=imie, last_name=nazwisko)
        p.save()
        return HttpResponse(f'probujesz dodac {imie} {nazwisko} do bazy')


def wyswietlanie_osob(request):
    osoby = Person.objects.all()
    return render(request, 'Cosby.html', context={'persons':osoby})

def osoba(request, id):
    o = Person.objects.get(id=id)
    return render(request, 'o.html', {'osoba':o})