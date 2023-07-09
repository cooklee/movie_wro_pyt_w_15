import random
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from movie_app.models import Person, Genre


class IndexView(View):

    def get(self, request):
        return HttpResponse("Witaj")

    def post(self, request):
        return HttpResponse('do widzenia')


class IndexViewTemplate(View):

    def get(self, request):
        return render(request, 'base.html',)


class ShowElementOfTheList(View):

    def get(self, request):
        lst = ['ala', 'ma', 'kota', 1, 2, 15]
        return render(request, 'lista.html', {'imie':'sławek', 'lista':lst})

class AddPersonView(View):

    def get(self, request):
        return render(request, 'person_form.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Person.objects.create(first_name=first_name, last_name=last_name)
        return redirect('add_person')

class AddGenreView(View):

    def get(self, request):
        genres = Genre.objects.all()
        return render(request, 'genre_form.html', {'genres':genres})

    def post(self, request):
        name = request.POST.get('name')
        Genre.objects.create(name=name)
        return redirect('add_genre')


class LosujView(View):

    def get(self, request, swinka, zajaczek):
        return HttpResponse(str(random.randint(swinka, zajaczek)))

class PersonsView(View):

    def get(self, request):
        persons = Person.objects.all()
        return render(request, 'person_list.html', {'persons':persons})


class PersonDetailView(View):

    def get(self, request, id):
        person = Person.objects.get(pk=id)
        return render(request, 'person_detail.html', {'person':person})


class GenreUpdateView(View):

    def get(self, request, pk):
        genres = Genre.objects.all()
        genre = Genre.objects.get(pk=pk)
        return render(request, 'genre_form.html', {'genre':genre, 'genres':genres})

    def post(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        name =request.POST.get('name')
        genre.name = name
        genre.save()
        return redirect('add_genre')