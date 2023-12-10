from django.core.management.base import BaseCommand, CommandError

from polka.models import Cart, CartItem


class Command(BaseCommand):


    def handle(self, *args, **options):
       carts = Cart.objects.all()
       for cart in carts:
           books = cart.books.all()
           for book in books:
               CartItem.objects.create(cart=cart, book=book)