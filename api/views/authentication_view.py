from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.authtoken import (views, models)
from rest_framework.response import Response

from api.models import User
from api.serializers import UserSerializer
from api.utils import encrypt_password


class CredentialSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        attrs["password"] = encrypt_password(attrs["password"])
        return attrs


class UserAuthTokenView(views.ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        credential_serializer = CredentialSerializer(data=request.data)
        credential_serializer.is_valid(raise_exception=True)
        data = credential_serializer.validated_data
        instance = get_object_or_404(User, email=data["email"], password=data["password"])
        token, _ = models.Token.objects.get_or_create(user=instance)
        serializer = UserSerializer(instance, context={"request": request})
        return Response({"user": serializer.data, "token": token.key}, status=status.HTTP_200_OK)
