from rest_framework import serializers

from api.models import Response, Photo


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

        request = self.context.get("request")
        if request and request.user.is_authenticated:
            may_be_existing_vote = votes.filter(owner=request.user)
            data["info"] = {
                "is_already_voted": may_be_existing_vote.exists(),
                "nature": may_be_existing_vote.first().is_upvote
            }

        return data
