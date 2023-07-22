import random
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from movie_app.forms import AddReviewForm
from movie_app.models import Person, Genre, Movie


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
        Person.objects.create(**request.POST)
        return redirect('add_person')

class AddGenreView(UserPassesTestMixin, View):

    def test_func(self):
        user = self.kwargs['id']
        return user.username == 'cooklee'

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


class AddReviewToMovieView(View):

    def get(self, request, id_movie):
        form = AddReviewForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request, id_movie):
        form = AddReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            movie = Movie.objects.get(pk=id_movie)
            user = request.user
            review.user = user
            review.movie = movie
            review.save()
            return redirect('index_template')
        return render(request, 'form.html', {'form': form})

class MovieDetailView(View):

    def get(self, request, id):
        movie = Movie.objects.get(pk=id)
        return render(request, 'movie_detail.html', {'movie':movie})