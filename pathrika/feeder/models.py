from django.db import models


class Feed(models.Mode):
    title = models.CharField(max_length=1024, blank=True)
    subtitle = models.TextField(blank=True)
    link = models.URLField()
    href = models.URLField()
    updated = models.DateTimeField()
    processed = models.BooleanField(default=False)

class Article(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=1024, blank=True)
    link = models.URLField()
    href = models.URLField()
    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=256, blank=True)
    tags = models.CharField(max_length=256, blank=True)
    published = models.DateTimeField()
