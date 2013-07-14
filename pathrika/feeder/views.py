from django.shortcuts import render

from feeder.forms import UrlForm
from feeder.models import Feed, Article


def add_feed(request):
    success = False
    if request.method == 'POST':
        urlform = UrlForm(request.POST)
        if urlform.is_valid():
            feed = Feed.objects.create()
            feed.rss_url = urlform.cleaned_data['url']
            feed.save()
            success = True
    else:
        urlform = UrlForm()
    return render(request, "add_feed.html",
                  {'form': urlform,
                   'success': success})


def home(request):
    feeds = Feed.objects.all()
    articles = Article.objects.all()
    context = {
        'feeds': feeds,
        'articles': articles,
    }
    return render(request, 'home.html', context)
