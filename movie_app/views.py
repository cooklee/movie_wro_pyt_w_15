import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from movie_app.models import Person


class IndexView(View):

    def get(self, request):
        return HttpResponse("Witaj")

    def post(self, request):
        return HttpResponse('do widzenia')


class IndexViewTemplate(View):

    def get(self, request):
        return render(request, 'base.html')


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