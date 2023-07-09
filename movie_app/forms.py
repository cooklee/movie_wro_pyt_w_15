from django import forms
from django.core.exceptions import ValidationError

from movie_app.models import Person, Genre, Movie, Review
from movie_app.validators import check_len


def five_letter(value):
    if len(value) == 5:
        raise ValidationError("Tylko 5 liter !!!!")


def check_if_capita(value):
    if not value[0].isupper():
        raise ValidationError("nie jest wielką litera")


def check_if_ends_with_k(value):
    if value[-1] in ('k', "K"):
        raise ValidationError('kończy sie na K')





class AddPersonForm(forms.Form):
    first_name = forms.CharField(validators=[five_letter])
    last_name = forms.CharField(validators=[check_len, check_if_capita, check_if_ends_with_k])
    year = forms.IntegerField()


class AddMovieForm(forms.Form):
    title = forms.CharField()
    year = forms.IntegerField()
    director = forms.ModelChoiceField(queryset=Person.objects.all())
    screenplay = forms.ModelChoiceField(queryset=Person.objects.all())
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all())


class AddMovieModelForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        director = cleaned_data.get('director')
        movie_year = cleaned_data.get('year')
        if director is not None:
            if director.year >= movie_year:
                raise ValidationError("rezyser młodszy od filmy")
        return cleaned_data

    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {
            'genres': forms.CheckboxSelectMultiple
        }


class AddReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['text']