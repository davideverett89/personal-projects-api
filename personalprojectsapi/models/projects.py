"""This class defines the projects I have worked on in class."""

from django.db import models
# from django.db.models import F
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

class Project(models.Model):

    """This class defines the projects I have worked on in class."""

    available = models.BooleanField()
    description = models.CharField(max_length=500)
    github_url = models.CharField(max_length=500)
    screenshot = models.CharField(max_length=500)
    technologies_used = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title
