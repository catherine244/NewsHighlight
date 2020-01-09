from flask import render_template
from . import main
from ..requests import get_top_news ,get_top_news_by_source, get_sources, get_news_by_category, search_news

rom flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_topnews, get_categories, get_newsupdates

 #Views
@main.route('/') 
def index():
     '''
    View root page function that returns the index page and its data
    '''
     #Getting top news and categorically arranged news
     top_articles = get_topnews('general-news')
     print(top_articles)
     biz_articles = get_categories('business')
     tech_articles = get_categories('technology')
     ent_articles = get_categories('entertainment')
     sprt_articles = get_categories('sports')
     title = 'NEWSHIGHLIGHT'
     return render_template('index.html', title = title, google_news = top_articles, biz = biz_articles, tech = tech_articles, ent = ent_articles, sprt = sprt_articles)


@main.route('/update/<id>')
def article(id):
    detz_articles = get_newsupdates(id)
    print(detz_articles)
    return render_template('news.html',detz = detz_articles)
@main.route("/")
def index():
    top_news = get_top_news()
    news_source = get_sources()
    news = get_top_news()
    categories = ["business",
                "entertainment",
                "general",
                "health",
                "science",
                "sports",
                "technology"
                ]
    return render_template("index.html", 
                            top_news = top_news,
                            sources = news_source,
                            news = news,
                            categories = categories)


@main.route("/search/<query>")
def search(query):
    search_articles = search_news(query)
    categories = ["business",
                "entertainment",
                "general",
                "health",
                "science",
                "sports",
                "technology"
                ]
    return render_template("search.html",
                            search_articles = search_articles,
                            categories = categories)

