from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    password = models.CharField(max_length=64, default="qwerty")
    username = models.CharField(max_length=64, null=True, unique=True)
    # cart

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} {self.author}"

class Publisher(models.Model):
    name = models.CharField(max_length=123)
    city = models.CharField(max_length=123)


    def __str__(self):
        return f"{self.name} {self.city}"


class Cart(models.Model):
    owner = models.OneToOneField(Person, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

