from users.views import SignUpView,LoginView,UserList,UserDeleteView,UserDetailView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views

urlpatterns = [
    path("list/", UserList.as_view(), name="list"),
    path("list/<int:pk>/", UserDetailView.as_view(), name="detail"),
    path("list/<int:pk>/delete/", UserDeleteView.as_view(), name="list"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
