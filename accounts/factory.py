import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model
from .models import CustomUser, Employee

User = get_user_model()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.Sequence(lambda n: f'{n}asa@gmail.com')
    password = factory.PostGenerationMethodCall("set_password", 'test1234')
    is_active = True


class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model = Employee

    first_name = factory.Sequence(lambda n: f"Jon_{n}")
    last_name = factory.Sequence(lambda n: f"Doe_{n}")
    position = factory.Sequence(lambda n: f"Position_{n}")
    link_instagram = factory.Sequence(lambda n: f"https://www.instagram.com/employee{n}")
    link_telegram = factory.Sequence(lambda n: f"https://t.me/employee{n}")

