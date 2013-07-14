var app = app || {};

app.Article = Backbone.Model.extend({
  defaults: {
    title: '',
    summary: '',
    content: '',
    author: ''
  }
});
