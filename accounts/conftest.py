import pytest
from django.contrib.auth import get_user_model
from .factory import UserFactory, EmployeeFactory



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



