"""
URL configuration for biblioteka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from polka import views
from accounts import views as account_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_django),
    path('ilosc/<int:ilosc>/', views.napis),
    path('tabliczla/<int:a>/<int:b>/', views.tabliczka),
    path("dodaj_osobe/", views.dodaj_osobe),
    path('osoby/', views.wyswietlanie_osob),
    path('osoby/<int:id>/', views.osoba),
    path('dodaj_ksiazke/', views.dodaj_ksiazke),
    path('ksiazki/', views.ksiazki),
    path('dodaj_wydawce/', views.AddPublisher),
    path('wydawcy/', views.show_publishers),
    path('login/', account_view.login),
    path('logout/', account_view.logout),
    path("add_book_to_cart/<int:book_id>/", views.add_book_to_cart),
    path('show_cart/', views.show_cart),
    path('', views.index)
]
