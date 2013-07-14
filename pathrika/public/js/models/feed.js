var app = app || {};

app.Feed = Backbone.Model.extend({
  defaults: {
    title: '',
    subtitle: '',
    url: '',
    rss_url: ''
  }
});
