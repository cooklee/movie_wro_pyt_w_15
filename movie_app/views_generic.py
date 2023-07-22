from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView

from movie_app.models import Person, Movie


class AddPersonGenericView(CreateView):
    model = Person
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('person_list')


class UpdateViewMovie(UpdateView):
    model = Movie
    fields = '__all__'
    template_name = 'form.html'


    def get_success_url(self):
        return reverse('generic_update_movie_view', kwargs={'pk': self.kwargs['pk']})


class MovieGenericListView(UserPassesTestMixin, ListView):

    def test_func(self):
        if self.request.user.username.startswith('cooklee'):
            return True
        return False

    permission_required = ['movie_app.view_movie']
    model = Movie
    template_name = 'movie_list.html'
