from rest_framework import serializers

from twitter_laboratory.models.communication_app import CommunicationApp


class CommunicationAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationApp
        fields = '__all__'
