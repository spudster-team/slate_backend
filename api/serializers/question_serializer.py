from rest_framework import serializers

from api.models import Question, Photo, Tag
from .response_serializer import ResponseSerializer
from .tag_serializer import TagSerializer


class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)
    photo = serializers.ImageField(required=False, allow_null=True, allow_empty_file=True)
    response = ResponseSerializer(read_only=True, many=True)
    tag = TagSerializer(required=False, many=True)

    class Meta:
        model = Question
        fields = ("id", "owner", "title", "content", "date_posted", "photo", "response", "tag")

    def validate(self, attrs):
        attrs["owner"] = self.context.get("request").user
        attrs["photo"] = Photo.objects.create(path=attrs["photo"]) if attrs.get("photo") else None

        tags: list[Tag] = []
        for tag in attrs["tag"]:
            may_be_existing_tag = Tag.objects.filter(title=tag.title)
            if may_be_existing_tag.exists():
                tags.append(may_be_existing_tag.first())
            else:
                tags.append(Tag.objects.create(**tag))
        attrs["tag"] = tags

        return attrs

    def to_representation(self, instance: Question):
        data = super().to_representation(instance)
        votes = instance.vote.all()
        data["up_vote"] = votes.filter(is_upvote=True).count()
        data["down_vote"] = votes.filter(is_upvote=False).count()
        data["n_response"] = instance.response.count()

        request = self.context.get("request")
        if request and request.user.is_authenticated:
            may_be_existing_vote = votes.filter(owner=request.user)
            data["info"] = {
                "is_already_voted": may_be_existing_vote.exists(),
                "nature": may_be_existing_vote.first().is_upvote
            }

        return data
