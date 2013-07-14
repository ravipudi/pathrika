from tastypie.resources import ModelResource

from feeder.models import Feed, Article


class FeedResource(ModelResource):
    pass

    class Meta:
        queryset = Feed.objects.all()


class ArticleResource(ModelResource):
    pass

    class Meta:
        queryset = Article.objects.all()
