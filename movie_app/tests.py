import pytest
from django.test import Client
# Create your tests here.
from django.urls import reverse


def test_index():
    url = reverse('index')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
    assert 'Witaj' in str(response.content)


@pytest.mark.django_db
def test_person_list_view(persons):
    url = reverse('person_list')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['persons'].count() == len(persons)
    for person in persons:
        assert person in response.context['persons']