from django.contrib.auth.models import User
from rest_framework import generics, status
from .serializers import UserSerializer
from rest_framework.response import Response
from .serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


class RegisterUser(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    authentication_classes = ()


class LoginUser(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutUser(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "Successfully logged out."},
                status=status.HTTP_205_RESET_CONTENT,
            )
        except Exception as e:
            return Response(
                {"error": "Invalid token or logout failed."},
                status=status.HTTP_400_BAD_REQUEST,
            )
