from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)

from twitter_laboratory.models.communication_app import CommunicationApp
from twitter_laboratory.serializers.communication_app_serializer import CommunicationAppSerializer


class CommunicationAppListCreateAPIView(ListCreateAPIView):
    serializer_class = CommunicationAppSerializer
    queryset = CommunicationApp.objects.all()


class CommunicationAppRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommunicationAppSerializer
    queryset = CommunicationApp.objects.all()
