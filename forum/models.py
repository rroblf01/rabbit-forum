from re import U

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Forum(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(
        Category, related_name="forums", on_delete=models.CASCADE
    )
    topics = models.ManyToManyField(Topic, related_name="forums")

    def __str__(self):
        return self.title


class Post(models.Model):
    forum = models.ForeignKey(Forum, related_name="posts", on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    reply = models.ForeignKey(
        "self", null=True, blank=True, related_name="replies", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post in {self.forum.title} at {self.created_at}"
