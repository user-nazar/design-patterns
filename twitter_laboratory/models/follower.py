from django.db import models


class Follower(models.Model):
    user_name = models.CharField(max_length=30, null=False)
    biography = models.CharField(max_length=90, null=True)
