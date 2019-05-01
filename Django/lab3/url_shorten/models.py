from django.db import models
from random import choice, shuffle


class URL(models.Model):
    long_url = models.URLField(max_length=500, unique=True)
    short = models.CharField(max_length=8)

    def __str__(self):
        return self.long
