var app = app || {};

var FeedList = Backbone.Collection.extend({
  model: app.Feed,

  url: function () { return '/feeds/'; }
});

app.Feeds = new FeedList();
