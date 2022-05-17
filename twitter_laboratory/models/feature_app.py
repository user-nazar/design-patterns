from django.db import models


class FeatureApp(models.Model):
    name = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=30, null=True)
    quantity = models.CharField(max_length=80, null=False)

    def set_description(self, description):
        self.description = description
        return True
