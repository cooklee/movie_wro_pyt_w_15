import pytest
from django.contrib.auth.models import User

from movie_app.models import Person, Genre


@pytest.fixture
def persons():
    lst = []
    for x in range(10):
        p = Person.objects.create(first_name=x, last_name=x)
        lst.append(p)
    return lst


@pytest.fixture
def person():
    p = Person.objects.create(first_name='Slawek', last_name='Bo')
    return p


@pytest.fixture
def genres():
    lst = []
    for x in range(3):
        lst.append(Genre.objects.create(name=x))
    return lst

@pytest.fixture
def user():
    return User.objects.create(username='testowy')
