from django.db import models
from django.utils import timezone

# Create your models here.


class ToDo(models.Model):
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)  # nuke blank?

    def toggle(self):
        """ if completed true set to false and vis versa """
        self.completed = not self.completed
        if self.completed:
            self.completed_date = timezone.now()
        else:
            self.completed_date = None
        self.save()

    def __str__(self):
        return self.text
