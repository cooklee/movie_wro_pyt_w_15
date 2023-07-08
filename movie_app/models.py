from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    #movie_set
    #movie_set


class Genre(models.Model):
    name = models.CharField(max_length=128)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField()
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='directed_by')
    screenplay = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='writen')
    genres = models.ManyToManyField(Genre)
