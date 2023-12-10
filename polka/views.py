from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from polka.models import Person, Book, Publisher, Cart, CartItem


def index(request):
    user_id = request.session.get('user_id')
    if user_id is not None:
        user = Person.objects.get(pk=user_id)
    else:
        user = None
    return render(request, 'base.html', {'osoba':user})

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


def dodaj_ksiazke(request):
    if request.method == "GET":
        authors = Person.objects.all()
        response = render(request, 'add_book.html', {'authors':authors})
        return response

    title = request.POST.get('title')
    author_id = request.POST.get('author')
    autor = Person(id=author_id)
    b = Book(title=title, author=autor)
    b.save()
    return redirect('show_books')

def ksiazki(request):
    books = Book.objects.all()
    authors = Person.objects.all()
    author_id = request.GET.get('author', '')
    title = request.GET.get('title', '')
    if author_id != '':
        books =books.filter(author_id=author_id)
    books = books.filter(title__icontains=title)
    return render(request, 'books.html', {'books':books, 'authors':authors})


class UpdatePublisherView(View):

    def get(self, request, pk):
        publisher = Publisher.objects.get(pk=pk)
        return render(request, 'add_publisher.html', {'publisher':publisher})

    def post(self, request, pk):
        publisher = Publisher.objects.get(pk=pk)
        name = request.POST.get('name')
        city = request.POST.get('city')
        publisher.name = name
        publisher.city = city
        publisher.save()
        return redirect('show_publisher')


def AddPublisher(request):

    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        p = Publisher(name=name, city=city)
        p.save()

    return render(request, 'add_publisher.html')

def show_publishers(request):
    publishers = Publisher.objects.all()
    name = request.GET.get('name', '')
    city = request.GET.get('city', '')
    print(city, name)
    if name != "":
        publishers = publishers.filter(name__icontains=name)
    if city != "":
        publishers = publishers.filter(city__icontains=city)

    return render(request, 'publisher_list.html', {'publishers':publishers})


def add_book_to_cart(request,book_id):
    user_id = request.session.get('user_id')
    if user_id is None:
        login_url = reverse('login')
        add_book_to_cart_url = reverse('add_to_cart', kwargs={'book_id':book_id})
        return redirect(f'{login_url}?next={add_book_to_cart_url}')
    book = Book.objects.get(pk=book_id)
    user = Person.objects.get(pk=user_id)
    cart, created = Cart.objects.get_or_create(owner=user)
    cartitem, created = CartItem.objects.get_or_create(book=book, cart=cart)
    if not created:
        cartitem.amount += 1
        cartitem.save()
    messages.add_message(request, messages.INFO,f"udalo sie dodać książke {book.title} do koszyka")
    return redirect('show_books')


def show_cart(request):
    user_id = request.session.get('user_id')
    login_url = reverse('login')
    cart_url = reverse('show_card')
    if user_id is None:
        return redirect(f'{login_url}?next={cart_url}')
    cart = Cart.objects.get(owner_id=user_id)
    return render(request, 'cart_list.html', {'cart':cart})




