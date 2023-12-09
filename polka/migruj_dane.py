from polka.models import Person, Book


def migruj():
    books = Book.objects.all()
    for book in books:
        author = book.author
        imie, nazwisko = author.split(' ')
        person, created = Person.objects.get_or_create(first_name=imie, last_name=nazwisko)
        book.author2 = person
        book.save()