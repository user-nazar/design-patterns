from rest_framework import serializers

from twitter_laboratory.models.follower import Follower


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'
