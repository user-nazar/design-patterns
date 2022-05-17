import csv

from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from twitter_laboratory.models.feature_app import FeatureApp
from twitter_laboratory.serializers.feature_app_serializer import FeatureAppSerializer


class UploadDataCSVFile(ListCreateAPIView):
    serializer_class = FeatureAppSerializer
    queryset = FeatureApp.objects.all()

    def create(self, request, *args, **kwargs):
        file = request.data.get('feature_app')
        file_rows = [row.decode("utf-8") for row in file]
        reader = csv.reader(file_rows, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
        for feature_app in reader:
            if feature_app:
                request_data = format_data(feature_app)
                create_request_record(request_data)  # METHOD INJECTION
        return Response('Uploaded', status=status.HTTP_201_CREATED)


def format_data(feature_app):
    request_data = {"id": feature_app.pop(0),
                    "name": feature_app.pop(0),
                    "description": feature_app.pop(0),
                    "quantity": feature_app.pop(0),
                    }

    return request_data


def create_request_record(request_data):
    feature_app_serializer = FeatureAppSerializer(data=request_data)
    feature_app_serializer.is_valid(raise_exception=True)
    request_obj = feature_app_serializer.save()

    request_obj.save()

    return True
