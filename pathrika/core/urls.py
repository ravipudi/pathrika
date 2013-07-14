from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^add-feed/$',
        'feeder.views.add_feed',
        name='add-feed'),

    url('^$',
        TemplateView.as_view(template_name='index.html'),
        name='home'),
)
