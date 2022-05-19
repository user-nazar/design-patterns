from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from rest_framework.response import Response

from twitter_laboratory.models.feature_app import FeatureApp
from twitter_laboratory.serializers.feature_app_serializer import FeatureAppSerializer


class FeatureAppListCreateAPIView(ListCreateAPIView):
    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_serializer = self.get_serializer(data=request_data)
        request_serializer.is_valid(raise_exception=True)
        request_obj = request_serializer.save()
        print(request_data)
        app_quantity = request_data.pop('quantity')[0]
        print(app_quantity)
        request_obj.quantity = f'App quantity : {app_quantity}'  # Property Injection

        updated_description = f'Updated by : {request_obj.description}'
        request_obj.set_description(updated_description)  # Method Injection
        request_obj.save()
        return Response(request_serializer.data, status=status.HTTP_201_CREATED)

    serializer_class = FeatureAppSerializer
    queryset = FeatureApp.objects.all()


class FeatureAppRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FeatureAppSerializer
    queryset = FeatureApp.objects.all()
