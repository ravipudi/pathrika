from django.db import models


class Feed(models.Model):
    title = models.CharField(max_length=1024, blank=True)
    subtitle = models.TextField(blank=True)
    url = models.URLField()
    rss_url = models.URLField("RSS URL")
    updated = models.DateTimeField(null=True, blank=True)
    processed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class Article(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=1024, blank=True)
    url = models.URLField()
    rss_url = models.URLField("RSS URL")
    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=256, blank=True)
    tags = models.CharField(max_length=256, blank=True)
    published = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.title
