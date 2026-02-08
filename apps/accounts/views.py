from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import login, logout

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    AccountSerializer,
)

from django.middleware.csrf import get_token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(["GET"])
@permission_classes([AllowAny])
def csrf_token(request):
    return Response({"detail": "CSRF cookie set"})

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            AccountSerializer(user).data,
            status=status.HTTP_201_CREATED
        )


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        login(request, user)

        return Response(
            AccountSerializer(user).data,
            status=status.HTTP_200_OK
        )


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(
            {"detail": "Successfully logged out"},
            status=status.HTTP_200_OK
        )


class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(
            AccountSerializer(request.user).data,
            status=status.HTTP_200_OK
        )
