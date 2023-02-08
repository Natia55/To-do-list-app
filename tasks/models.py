from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
