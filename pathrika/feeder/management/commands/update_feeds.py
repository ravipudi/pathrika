import datetime
import calendar

from django.core.management.base import BaseCommand
import feedparser

from feeder.models import Feed, Article


class Command(BaseCommand):

    def handle(self, *args, **options):
        feeds = Feed.objects.all()
        for feed in feeds:
            f1 = feedparser.parse(feed.rss_url)
            if f1.get('bozo_exception'):
                self.stderr.write("error while trying to parse : " +
                                  str(f1.bozo_exception))

            if not feed.processed:
                feed.title = f1.feed.title
                feed.subtitle = f1.feed.subtitle
                feed.url = f1.feed.link
                feed.updated = datetime.datetime.fromtimestamp(
                    calendar.timegm(f1.feed.updated_parsed)
                )
                feed.processed = True
                feed.save()
                self.stdout.write("Successfully processed %s" % feed.rss_url)

            for entry in f1.entries:
                article, created = Article.objects.get_or_create(
                    feed=feed,
                    url=entry.link,
                    rss_url=entry.title_detail.base,
                )
                if created:
                    try:
                        article.title = entry.title
                        article.summary = entry.summary
                        article.content = entry.content
                        article.author = entry.author
                        article.published = datetime.datetime.fromtimestamp(
                            calendar.timegm(entry.published_parsed)
                        )
                        article.save()
                    except:
                        self.stdout.write("Error");
                    self.stdout.write("Successfully added %s in %s feed" %
                                      (entry.title, f1.feed.title))
