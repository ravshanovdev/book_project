import factory
from factory.django import DjangoModelFactory
from .models import Book


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Sequence(lambda n: f'Book {n}')
    price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    published_date = factory.Faker('date')
    description = factory.Faker('paragraph')



