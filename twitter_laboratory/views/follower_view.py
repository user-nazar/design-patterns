from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)

from twitter_laboratory.models.follower import Follower
from twitter_laboratory.serializers.follower_serializer import FollowerSerializer


class FollowerListCreateAPIView(ListCreateAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()


class FollowerRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
