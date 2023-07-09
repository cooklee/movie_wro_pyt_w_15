"""
URL configuration for Movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from movie_app import views, forms_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.IndexView.as_view(), name='index'),
    path("losuj/<int:swinka>/<int:zajaczek>/",views.LosujView.as_view(),name='losuj'),
    path("szablon/", views.IndexViewTemplate.as_view(), name='index_template'),
    path("lista/", views.ShowElementOfTheList.as_view(), name='lista'),
    path("addPerson/", views.AddPersonView.as_view(), name='add_person'),
    path("addgenre/", views.AddGenreView.as_view(), name='add_genre'),
    path("persons/", views.PersonsView.as_view(), name="person_list"),
    path("person/<int:id>/", views.PersonDetailView.as_view(), name="person_detail"),
    path("genre/<int:pk>/", views.GenreUpdateView.as_view(), name="genre_update"),
    path('add_person_form/', forms_views.AddPersonFormView.as_view(), name='add_person_form_view'),
    path('add_movie_form/', forms_views.AddMovieFormView.as_view(), name='add_movie_form_view'),
]
