from django.db import models


class URL(models.Model):
    # index = models.URLField(max_length=200, null=True)
    long_url = models.URLField(max_length=500, unique=True)
    short = models.CharField(max_length=8)

    def __str__(self):
        return self.long_url
