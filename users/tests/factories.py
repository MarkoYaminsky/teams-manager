from factory import LazyFunction, Sequence
from factory.django import DjangoModelFactory
from faker import Faker

from users.models import User

fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    name = LazyFunction(lambda: fake.name())
    surname = LazyFunction(lambda: fake.last_name())
    email = Sequence(lambda x: f"{fake.email()}{x}")
    password = "password"
