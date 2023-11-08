from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from api.models import User, Photo
from api.utils import encrypt_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    photo = serializers.ImageField(required=False, allow_null=True, allow_empty_file=True)

    class Meta:
        model = User
        fields = ("id", "email", "password", "first_name", "last_name", "photo")

    def validate(self, attrs):
        attrs["password"] = encrypt_password(attrs["password"])
        attrs["photo"] = Photo.objects.create(path=attrs["photo"]) if attrs.get("photo") else None
        return attrs


class UpdateUserSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False, allow_null=True, allow_empty_file=True)

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "photo")

    def validate(self, attrs):
        attrs["photo"] = Photo.objects.create(path=attrs["photo"]) if attrs.get("photo") else None
        return attrs


class BasicUserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "photo")
