from rest_framework import serializers
from django.utils.timesince import timesince

from api.models import Response, Photo
from api.serializers import PhotoSerializer


class ResponseSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)
    photo = serializers.ImageField(write_only=True, required=False, allow_null=True, allow_empty_file=True)
    data_posted = serializers.SerializerMethodField(method_name="get_time_since_posted")

    class Meta:
        model = Response
        fields = ("id", "owner", "content", "date_posted", "photo")

    def validate(self, attrs):
        attrs["owner"] = self.context.get("request").user
        attrs["photo"] = Photo.objects.create(path=attrs["photo"]) if attrs.get("photo") else None
        return attrs

    @staticmethod 
    def get_time_since_posted(obj):
        return timesince(obj.data_posted) 

    def to_representation(self, instance: Response):
        data = super().to_representation(instance)

        votes = instance.vote.all()
        data["up_vote"] = votes.filter(is_upvote=True).count()
        data["down_vote"] = votes.filter(is_upvote=False).count()

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
