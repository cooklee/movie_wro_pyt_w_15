from django import forms

from movie_app.models import Person, Genre


class AddPersonForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()

class AddMovieForm(forms.Form):
    title = forms.CharField()
    year = forms.IntegerField()
    director = forms.ModelChoiceField(queryset=Person.objects.all())
    screenplay = forms.ModelChoiceField(queryset=Person.objects.all())
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all())