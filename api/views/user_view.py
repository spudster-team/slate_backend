from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import User
from api.serializers import UserSerializer, UpdateUserSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        need_authentication = ["update", "destory", "retrieve"]
        if self.action in need_authentication:
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def get_serializer_context(self):
        return {"request": request}

    @action(detail=False)
    def most_active_user(self, request):
        most_active_users = User.objects.annotate(
            activity_count=Count("question") + Count("response")
        ).order_by("-activity_count").exclude(is_superuser=True)[:7]
        serializer = self.serializer_class(most_active_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        token, _ = Token.objects.get_or_create(user=instance)
        return Response({"user": serializer.data, "token": token.key}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(User, id=request.user.id)
        serializer = self.serializer_class(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(User, id=request.user.id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UpdateUserSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.update(user, serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
