import pytest
from django.contrib.auth import get_user_model
from accounts.factory import UserFactory, EmployeeFactory
from book.factory import BookFactory



@pytest.fixture
def user_admin(db):
    return UserFactory(is_superuser=True, is_staff=True)


@pytest.fixture
def user(db):
    return UserFactory()


@pytest.fixture
def employee(db):
    return EmployeeFactory()


@pytest.fixture
def multi_employees(db):
    return EmployeeFactory.create_batch(5)


@pytest.fixture
def book(db):
    return BookFactory()


@pytest.fixture
def multi_books(db):
    return BookFactory.create_batch(5)
