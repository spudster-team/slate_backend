from rest_framework import serializers
from django.utils.timesince import timesince

from api.models import Question, Photo, Tag
from . import PhotoSerializer
from .response_serializer import ResponseSerializer
from .tag_serializer import TagSerializer
from .user_serializer import UserSerializer


class QuestionSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    photo = serializers.ImageField(write_only=True, required=False, allow_null=True, allow_empty_file=True)
    response = ResponseSerializer(read_only=True, many=True)
    tag = TagSerializer(required=False, many=True)
    date_posted = serializers.SerializerMethodField(method_name="get_time_since_posted")

    class Meta:
        model = Question
        fields = ("id", "owner", "title", "content", "date_posted", "photo", "response", "tag")

    def validate(self, attrs):
        attrs["owner"] = self.context.get("request").user
        attrs["photo"] = Photo.objects.create(path=attrs["photo"]) if attrs.get("photo") else None

        tags: list[Tag] = []
        attrs_tags = attrs.get("tag")
        if attrs_tags:
            for tag in attrs_tags:
                may_be_existing_tag = Tag.objects.filter(title=tag.title)
                if may_be_existing_tag.exists():
                    tags.append(may_be_existing_tag.first())
                else:
                    tags.append(Tag.objects.create(**tag))
        attrs["tag"] = tags

        return attrs

    def create(self, validated_data):
        tag = validated_data.pop("tag")
        new_question: Question = Question.objects.create(**validated_data)
        new_question.tag.add(*tag)
        return new_question

    def update(self, instance, validated_data):
        tags = validated_data.get("tag")
        instance.vote = validated_data.get("vote", instance.vote)
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.photo = validated_data.get("photo", instance.photo)
        if tags is not None:
            instance.tag.add(*tags)
        instance.save()
        return instance

    @staticmethod 
    def get_time_since_posted(obj):
        return timesince(obj.date_posted)

    def to_representation(self, instance: Question):
        data = super().to_representation(instance)
        votes = instance.vote.all()

        data["up_vote"] = votes.filter(is_upvote=True).count()
        data["down_vote"] = votes.filter(is_upvote=False).count()
        data["n_response"] = instance.response.count()

        request = self.context.get("request")
        if request and request.user.is_authenticated:
            may_be_existing_vote = votes.filter(owner=request.user)
            if may_be_existing_vote.exists():
                data["info"] = {
                    "is_already_voted": True,
                    "is_upvote": may_be_existing_vote.first().is_upvote
                }
        data["photo"] = PhotoSerializer(instance.photo, context={"request": request}).data

        return data
