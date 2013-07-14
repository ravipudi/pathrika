var app = app || {};

var ArticleList = Backbone.Collection.extend({
  model: app.Article
});

app.Articles = new ArticleList();
