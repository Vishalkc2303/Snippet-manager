from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Snippet(models.Model):
    VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]

    title = models.CharField(max_length=200)
    code = models.TextField()  # Can store 1000+ lines easily
    description = models.TextField(blank=True, null=True)
    visibility = models.CharField(max_length=7, choices=VISIBILITY_CHOICES, default='public')

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # Relationships
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # ✅ Save/Bookmark Feature
    saved_by = models.ManyToManyField(User, related_name='saved_snippets', blank=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"
