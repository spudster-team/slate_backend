from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=20, null=False, unique=True)

    def __str__(self):
        return self.title
