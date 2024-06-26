from django.urls import path

from users.views import UserListCreateApi, UserRetrieveUpdateDestroyApi

app_name = "users"

urlpatterns = [
    path("", UserListCreateApi.as_view(), name="user-list-create"),
    path("<int:user_id>/", UserRetrieveUpdateDestroyApi.as_view(), name="user-retrieve-update-destroy"),
]
