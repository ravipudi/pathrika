var app = app || {};

var FeedView = Backbone.View.extend({
  el: '#articles',

  feedsTemplate: _.template( $('#feed-list') ),

  events: {
    'click .feed': 'showFeedArticles',
  },

  initialize: function () {
    this.listenTo(app.Feeds, 'add', this.addOne);
    this.listenTo(app.Feeds, 'reset', this.addAll);

    app.Feeds.fetch();
  },

  render: function () {
  }
});
