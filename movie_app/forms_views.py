from django.shortcuts import render, redirect
from django.views import View

from movie_app.forms import AddPersonForm, AddMovieForm
from movie_app.models import Person, Movie


class AddPersonFormView(View):

    def get(self, request):
        form = AddPersonForm()
        return render(request, 'form.html', {'form':form})


    def post(self, request):
        form = AddPersonForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            Person.objects.create(first_name=first_name, last_name=last_name)
            return redirect('person_list')
        return render(request, 'form.html', {'form': form})


class AddMovieFormView(View):

    def get(self, request):
        form = AddMovieForm()
        return render(request, 'form.html', {'form':form})


    def post(self, request):
        form = AddMovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            year = form.cleaned_data.get('year')
            director = form.cleaned_data.get('director')
            screenplay = form.cleaned_data.get('screenplay')
            m = Movie.objects.create(title=title, year=year, director=director, screenplay=screenplay)
            generes = form.cleaned_data.get('genre')
            m.genres.set(generes)
            return redirect('person_list')
        return render(request, 'form.html', {'form': form})