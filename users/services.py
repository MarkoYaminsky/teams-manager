from typing import Any, Iterable, Optional

from django.contrib.auth import get_user_model
from django.db.models import Q, QuerySet

from common.services import update_instance
from users.models import Team

User = get_user_model()


def get_all_users(*args: Q, **kwargs: Any) -> QuerySet[User]:
    return User.objects.filter(*args, **kwargs)


def create_user(
    name: str, surname: str, email: str, password: str, teams: Optional[Iterable[Team]] = None, **kwargs: Any
) -> User:
    user = User.objects.create(name=name, surname=surname, email=email, **kwargs)
    user.set_password(password)
    user.save()

    if teams is not None:
        user.teams.set(teams)

    return user


def update_user(user: User, **kwargs: Any) -> None:
    update_instance(instance=user, data=kwargs)


def delete_user(user: User) -> None:
    user.delete()


def get_all_teams(*args: Q, **kwargs: Any) -> QuerySet[Team]:
    return Team.objects.filter(*args, **kwargs)


def create_team(name: str, people: Optional[Iterable[User]] = None) -> Team:
    team = Team.objects.create(name=name)

    if people is not None:
        team.people.set(people)

    return team


def update_team(team: Team, **kwargs: Any) -> None:
    update_instance(instance=team, data=kwargs)


def delete_team(team: Team) -> None:
    team.delete()


def add_user_to_team(user: User, team: Team) -> None:
    team.people.add(user)


def remove_user_from_team(user: User, team: Team) -> None:
    team.people.remove(user)
