from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from tastypie.api import Api

from feeder.api import ArticleResource, FeedResource

urlpatterns = patterns(
    '',
    url(r'^add-feed/$',
        'feeder.views.add_feed',
        name='add-feed'),

    url('^$',
        #TemplateView.as_view(template_name='index.html'),
        'feeder.views.home',
        name='home'),
)


v1_api = Api(api_name='v1')
v1_api.register(ArticleResource())
v1_api.register(FeedResource())

urlpatterns += patterns(
    '',
    (r'^api/',
     include(v1_api.urls)),
)
