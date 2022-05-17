from rest_framework import serializers

from twitter_laboratory.models.feature_app import FeatureApp


class FeatureAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureApp
        fields = '__all__'
