from django.urls import path

from .views import (
    FollowAPIView,
    FollowersListAPIView,
    FollowingListAPIView,
    UserListAPIView,
    UserRetrieveUpdateDeleteAPIView,
    UserRegisterAPIView,
    UserLoginAPIView, confirm_email,
)


urlpatterns = [
    path("", UserListAPIView.as_view()),
    path("<str:username>/", UserRetrieveUpdateDeleteAPIView.as_view()),
    path("<str:username>/follow/", FollowAPIView.as_view()),
    path("<str:username>/followers/", FollowersListAPIView.as_view()),
    path("<str:username>/following/", FollowingListAPIView.as_view()),
    path("auth/register/", UserRegisterAPIView.as_view()),
    path("auth/login/", UserLoginAPIView.as_view()),
    path("auth/email/confirm/<str:token>/", confirm_email),
]
