import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime


@pytest.mark.django_db
def test_admin_can_add_book(admin_user):
    client = APIClient()
    client.force_authenticate(admin_user)

    url = reverse('add-book')

    data = {
        'title': 'Ufq',
        'price': 45.45,
        'description': 'A book about Ufq'
    }

    response = client.post(url, data, format='multipart')

    assert response.status_code == 201
    assert response.data['title'] == 'Ufq'


@pytest.mark.dajngo_db
def test_regular_user_cannot_add_book(user):
    client = APIClient()
    client.force_authenticate(user)

    url = reverse('add-book')

    data = {
        'title': 'Ufq',
        'price': 45.45,
        'description': 'A book about Ufq'
    }

    response = client.post(url, data, format='multipart')

    assert response.status_code == 403


@pytest.mark.django_db
def test_get_all_book(user, multi_books):
    client = APIClient()
    client.force_authenticate(user)

    url = reverse('get-book')

    response = client.get(url, format='multipart')

    assert response.status_code == 200
    assert len(response.data) == len(multi_books)


@pytest.mark.django_db
def test_get_single_book(user, book):
    client = APIClient()
    client.force_authenticate(user)

    url = reverse('get-book') + f'?pk={book.id}'

    response = client.get(url, format='multipart')

    assert response.status_code == 200
    assert response.data['title'] == book.title



@pytest.mark.django_db
def test_admin_can_update_book(admin_user, book):
    client = APIClient()
    client.force_authenticate(admin_user)

    url = reverse('update-book', kwargs={'pk': book.id})
    data = {
        'title': 'changed'
    }

    response = client.patch(url, data, format='multipart')

    assert response.status_code == 200
    assert response.data['title'] == 'changed'


@pytest.mark.django_db
def test_regular_user_cannot_update_book(user, book):
    client = APIClient()
    client.force_authenticate(user)

    url = reverse('update-book', kwargs={'pk': book.id})
    data = {
        'title': 'changed'
    }

    response = client.patch(url, data, format='multipart')

    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_can_delete_book(admin_user, book):
    client = APIClient()
    client.force_authenticate(admin_user)

    url = reverse('delete-book', kwargs={'pk': book.id})

    response = client.delete(url, format='multipart')

    assert response.status_code == 204


@pytest.mark.django_db
def test_regular_user_cannot_delete_book(user, book):
    client = APIClient()
    client.force_authenticate(user)

    url = reverse('delete-book', kwargs={'pk': book.id})

    response = client.delete(url, format='multipart')

    assert response.status_code == 403














