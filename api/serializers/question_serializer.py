from rest_framework import serializers

from api.models import Question, Photo
from .response_serializer import ResponseSerializer


class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)
    photo = serializers.ImageField(required=False, allow_null=True, allow_empty_file=True)
    response = ResponseSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ("id", "owner", "title", "content", "date_posted", "photo", "response")

    def validate(self, attrs):
        attrs["owner"] = self.context.get("request").user
        attrs["photo"] = Photo.objects.create(path=attrs["photo"]) if attrs.get("photo") else None
        return attrs

    def to_representation(self, instance: Question):
        data = super().to_representation(instance)
        votes = instance.vote.all()
        data["up_vote"] = votes.filter(is_upvote=True).count()
        data["down_vote"] = votes.filter(is_upvote=False).count()
        data["n_response"] = instance.response.count()
        return data
