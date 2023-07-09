from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField()
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='directed_by')
    screenplay = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='writen')
    genres = models.ManyToManyField(Genre)
