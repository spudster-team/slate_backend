from django.db import models


class Vote(models.Model):
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    is_upvote = models.BooleanField()
    date_posted = models.DateTimeField(auto_now_add=True)
