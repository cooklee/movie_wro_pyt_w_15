from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


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
