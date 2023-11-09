from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .authentication_view import UserAuthTokenView
from .question_view import QuestionView
from .response_view import ResponseView
from .user_view import UserView
from ..models import Tag, Photo
from ..serializers import TagSerializer, PhotoSerializer


@api_view(["GET"])
def get_all_tags(request):
    if request.method == "GET":
        instance = Tag.objects.all()
        serializer = TagSerializer(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_all_photo(request):
    if request.method == "GET":
        instance = Photo.objects.all()
        serializer = PhotoSerializer(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
