from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=123)
    last_name = models.CharField(max_length=123)
    #movie_set

class movie(models.Model):
    title = models.CharField(243)
    director = models.ForeignKey(Person,
                                 related_name='directed_by')
    screen_play = models.ForeignKey(Person)