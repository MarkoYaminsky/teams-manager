from django.urls import path

from users.views import (
    TeamListCreateApi,
    TeamRetrieveUpdateDestroyApi,
    UserListCreateApi,
    UserRetrieveUpdateDestroyApi,
)

app_name = "users"

urlpatterns = [
    path("", UserListCreateApi.as_view(), name="user-list-create"),
    path("<int:user_id>/", UserRetrieveUpdateDestroyApi.as_view(), name="user-retrieve-update-destroy"),
    path("teams/", TeamListCreateApi.as_view(), name="team-list-create"),
    path("teams/<int:team_id>/", TeamRetrieveUpdateDestroyApi.as_view(), name="team-retrieve-update-destroy"),
]
