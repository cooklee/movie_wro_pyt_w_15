import pytest

from movie_app.models import Person


@pytest.fixture
def persons():
    lst = []
    for x in range(10):
        p = Person.objects.create(first_name=x, last_name=x)
        lst.append(p)
    return lst