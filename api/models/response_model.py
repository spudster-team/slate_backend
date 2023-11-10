from django.db import models


class Response(models.Model):
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey("Photo", on_delete=models.CASCADE, null=True, blank=True)
    vote = models.ManyToManyField("Vote", blank=True)