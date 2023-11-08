from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Response as ModelResponse, Vote
from api.serializers import ResponseSerializer, VoteSerializer


class ResponseView(ModelViewSet):
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(ModelResponse, owner=request.user, id=kwargs.get("id"))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        instance = get_object_or_404(ModelResponse, owner=request.user, id=kwargs.get("id"))
        serializer.update(instance, serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    @action(detail=False)
    def voting(self, request, **kwargs):
        vote_serializer = VoteSerializer(data=request.data, context={"request": request})
        vote_serializer.is_valid(raise_exception=True)
        instance: ModelResponse = get_object_or_404(ModelResponse, id=kwargs.get("id"))
        may_be_existing_vote = instance.vote.filter(owner=request.user)
        if may_be_existing_vote.exists():
            the_vote: Vote = may_be_existing_vote.first()
            if the_vote.is_upvote != vote_serializer.validated_data["is_upvote"]:
                the_vote = vote_serializer.validated_data["is_upvote"]
                the_vote.save()
            else:
                instance.vote.remove(the_vote)
        else:
            instance.vote.add(vote_serializer.save())
        return Response(status=status.HTTP_200_OK)
