"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from twitter_laboratory.views.csv_view import UploadDataCSVFile
from twitter_laboratory.views.communication_app_view import CommunicationAppListCreateAPIView, \
    CommunicationAppRetrieveUpdateAPIView
from twitter_laboratory.views.feature_app_view import FeatureAppListCreateAPIView, FeatureAppRetrieveUpdateAPIView
from twitter_laboratory.views.follower_view import FollowerListCreateAPIView, FollowerRetrieveUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('communication-apps/',  CommunicationAppListCreateAPIView.as_view()),
    path('communication-apps/<int:pk>/',  CommunicationAppRetrieveUpdateAPIView.as_view()),

    path('feature-apps/', FeatureAppListCreateAPIView.as_view()),
    path('feature-apps/<int:pk>/', FeatureAppRetrieveUpdateAPIView.as_view()),

    path('followers/', FollowerListCreateAPIView.as_view()),
    path('followers/<int:pk>/', FollowerRetrieveUpdateAPIView.as_view()),

    path('test_csv/', UploadDataCSVFile.as_view()),
]
