from rest_framework import serializers

from api.models import Response, Photo
from .vote_serializer import VoteSerializer


class ResponseSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)
    photo = serializers.ImageField(required=False, allow_null=True, allow_empty_file=True)

    class Meta:
        model = Response
        fields = ("id", "owner", "content", "date_posted", "photo")

    def validate(self, attrs):
        attrs["owner"] = self.context.get("request").user
        attrs["photo"] = Photo.objects.create(path=attrs["photo"]) if attrs.get("photo") else None
        return attrs

    def to_representation(self, instance: Response):
        data = super().to_representation(instance)
        votes = instance.vote.all()
        data["up_vote"] = votes.filter(is_upvote=True).count()
        data["down_vote"] = votes.filter(is_upvote=False).count()
        return data
