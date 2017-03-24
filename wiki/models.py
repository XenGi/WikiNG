from django.db import models


class Page(models.Model):

    uuid = models.UUIDField(unique=True)
    name = models.CharField(max_length=255)

    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
