import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    url = reverse('register')
    data = {
        'username': 'test_user',
        'email': "asas@gmail.com",
        'password': 'uniquepassword123',
        'password2': 'uniquepassword123'
    }

    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data['username'] == 'test_user'


@pytest.mark.django_db
def test_login_user(user):
    client = APIClient()
    url = reverse('login')

    data = {
        'email': user.email,
        'password': 'test1234'
    }

    response = client.post(url, data, format='json')

    assert response.status_code == 200
    assert "access" in response.data
    assert 'refresh' in response.data


@pytest.mark.django_db
def test_add_employee(admin_user):
    client = APIClient()
    client.force_authenticate(admin_user)

    url = reverse('add-employee')
    data = {
        'first_name': "John",
        'last_name': 'Doe',
        'position': 'Developer',
        'link_instagram': 'https://www.instagram.com/johndoe/',
        'link_telegram': 'https://t.me/johndoe'
    }

    response = client.post(url, data, format='multipart')

    assert response.status_code == 201
    assert response.data['first_name'] == 'John'



@pytest.mark.django_db
def test_get_all_employees(user, multi_employees):
    client = APIClient()
    client.force_authenticate(user)

    url = reverse('employee-list')

    response = client.get(url, format='json')

    assert response.status_code == 200
    assert len(response.data) == len(multi_employees)


@pytest.mark.django_db
def test_detail_employee(user, employee):
    client = APIClient()
    client.force_authenticate(user)

    url = reverse('employee-detail', kwargs={'pk': employee.id})

    response = client.get(url, format='json')

    assert response.status_code == 200
    assert response.data['first_name'] == employee.first_name
    assert response.data['last_name'] == employee.last_name
    assert response.data['position'] == employee.position
    assert response.data['link_instagram'] == employee.link_instagram
    assert response.data['link_telegram'] == employee.link_telegram


@pytest.mark.django_db
def test_delete_employee(admin_user, employee):
    client = APIClient()
    client.force_authenticate(admin_user)

    url = reverse('employee-delete', kwargs={'pk': employee.id})

    response = client.delete(url, format='json')

    assert response.status_code == 204


@pytest.mark.django_db
def test_update_employee(admin_user, employee):
    client = APIClient()
    client.force_authenticate(admin_user)

    url = reverse('update-employee', kwargs={'pk': employee.id})

    data = {
        'first_name': "James"
    }

    response = client.patch(url, data, format='multipart')

    assert response.status_code == 200
    assert response.data['first_name'] == 'James'








