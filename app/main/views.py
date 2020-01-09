from flask import render_template
from . import main
from ..requests import get_top_news ,get_top_news_by_source, get_sources, get_news_by_category, search_news



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




@main.route("/source/<source>")
def source(source):
    top_news_by_source = get_top_news_by_source(source)
    news_source = get_sources()
    categories = ["business",
                "entertainment",
                "general",
                "health",
                "science",
                "sports",
                "technology"
                ]
    return render_template("source.html",
                            sources = top_news_by_source,
                            news_source = news_source,
                            categories = categories,
                            source = source)

@main.route("/category/<category>")
def category(category):
    news_category = get_news_by_category(category)
    categories = ["business",
                "entertainment",
                "general",
                "health",
                "science",
                "sports",
                "technology"
                ]
    return render_template("category.html",
                            news_category = news_category,
                            categories = categories,
                            category = category)


