from factory import LazyFunction, Sequence
from factory.django import DjangoModelFactory
from faker import Faker

from users.models import Team, User

fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    name = LazyFunction(lambda: fake.name())
    surname = LazyFunction(lambda: fake.last_name())
    email = Sequence(lambda x: f"{fake.email()}{x}")
    password = "password"


class TeamFactory(DjangoModelFactory):
    class Meta:
        model = Team

    name = LazyFunction(lambda: fake.word())
