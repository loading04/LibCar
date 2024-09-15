from django.urls import path, include 
from .views import RegisterUser, LoginUser, LogoutUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", LogoutUser.as_view(), name="logout"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("auth/", include("rest_framework.urls"))

]
