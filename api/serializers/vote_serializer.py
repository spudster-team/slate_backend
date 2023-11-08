from rest_framework import serializers

from api.models import Vote


class VoteSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)

    class Meta:
        model = Vote
        fields = ("id", "owner", "date_posted")

    def validate(self, attrs):
        attrs["owner"] = self.context.get("request").user
        return attrs
