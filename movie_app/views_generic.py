from django.urls import reverse_lazy
from django.views.generic import CreateView

from movie_app.models import Person


class AddPersonGenericView(CreateView):

    model = Person
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('person_list')