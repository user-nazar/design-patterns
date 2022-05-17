from django.db import models


class CommunicationApp(models.Model):
    name = models.CharField(max_length=30, null=False)
    founder = models.CharField(max_length=60, null=False)
    year_of_creation = models.CharField(max_length=4, null=False)

