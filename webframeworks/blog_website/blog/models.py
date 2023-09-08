from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    class Status(models.TextChoices):
        # https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-choices-enum-types
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    when_created = models.DateTimeField(auto_now_add=True)
    when_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-when_created"]
        indexes = [
            models.Index(fields=['-when_created'])
        ]

    def __str__(self) -> str:
        return self.title
