from django.db import models


class Question(models.Model):
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey("Photo", on_delete=models.CASCADE, null=True, blank=True)
    vote = models.ManyToManyField("Vote", blank=True)
    response = models.ManyToManyField("Response", blank=True)
    tag = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title
