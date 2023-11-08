from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Question
from api.serializers import QuestionSerializer, ResponseSerializer, VoteSerializer


class QuestionView(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_permissions(self):
        need_authentication = ["update", "destory", "create", "respond"]
        if self.action in need_authentication:
            return [IsAuthenticated()]
        return [AllowAny()]

    def update(self, request, *args, **kwargs):
        instance = get_object_or_404(Question, id=kwargs.get("id"), owner=request.user)
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.update(instance, serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Question, id=kwargs.get("id"), owner=request.user)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Question, id=kwargs.get("id"))
        serializer = self.serializer_class(instance, context={"request": request})
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    @action(detail=False)
    def respond(self, request, **kwargs):
        response_serializer = ResponseSerializer(data=request.data, context={"request": request})
        response_serializer.is_valid(raise_exception=True)
        instance: Question = get_object_or_404(Question, id=kwargs.get("id"))
        instance.response.add(response_serializer.save())
        serializer = self.serializer_class(instance, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False)
    def voting(self, request, **kwargs):
        # Todo check if user already voted
        vote_serializer = VoteSerializer(data=request.data, context={"request": request})
        vote_serializer.is_valid(raise_exception=True)
        instance: Question = get_object_or_404(Question, id=kwargs.get("id"))
        instance.vote.add(vote_serializer.save())
        serializer = self.serializer_class(instance, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
