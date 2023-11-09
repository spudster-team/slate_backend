from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from api.models import User, Photo
from api.utils import encrypt_password
from .photo_seriaizer import PhotoSerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    photo = serializers.ImageField(write_only=True, required=False, allow_null=True, allow_empty_file=True)

    class Meta:
        model = User
        fields = ("id", "email", "password", "first_name", "last_name", "photo")

    def validate(self, attrs):
        attrs["password"] = encrypt_password(attrs["password"])
        attrs["photo"] = Photo.objects.create(path=attrs["photo"]) if attrs.get("photo") else None
        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        data["photo"] = PhotoSerializer(instance.photo, context={"request": request}).data
        return data


class UpdateUserSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(write_only=True, required=False, allow_null=True, allow_empty_file=True)

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "photo")

    def validate(self, attrs):
        attrs["photo"] = Photo.objects.create(path=attrs["photo"]) if attrs.get("photo") else None
        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        data["photo"] = PhotoSerializer(instance.photo, context={"request": request}).data
        return data


class BasicUserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "photo")
