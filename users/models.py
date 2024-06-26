from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_superuser(self, email: str, password: str, name: str, surname: str) -> "User":
        from .services import create_user

        return create_user(name=name, surname=surname, email=email, password=password, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("password", "name", "surname")

    objects = UserManager()

    @property
    def full_name(self) -> str:
        return f"{self.name} {self.surname}"

    def __str__(self) -> str:
        return self.full_name


class Team(models.Model):
    name = models.CharField(max_length=20)
    people = models.ManyToManyField(User, related_name="teams")

    def __str__(self) -> str:
        return f"Team {self.name}"
