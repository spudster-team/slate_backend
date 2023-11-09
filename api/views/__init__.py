from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .authentication_view import UserAuthTokenView
from .question_view import QuestionView
from .response_view import ResponseView
from .user_view import UserView
from ..models import Tag
from ..serializers import TagSerializer


@api_view(["GET"])
def get_all_tags(request):
    if request.method == "GET":
        instance = Tag.objects.all()
        serializer = TagSerializer(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
