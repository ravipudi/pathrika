from tastypie.resources import ModelResource

from feeder.models import Feed, Article


class FeedResource(ModelResource):
    class Meta:
        queryset = Feed.objects.all()


class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
