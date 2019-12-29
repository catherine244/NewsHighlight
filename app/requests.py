from app import app
import urllib.request,json
from .models import Source,Articles
# Getting api key
api_key = app.config['NEWS_API_KEY']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)
    return sources_results

def process_results(newsource_list):
    '''
    Function  that processes the new source result and transform them to a list of Objects

    Args:
        newsource_list: A list of dictionaries that contain news source details

    Returns :
        newsource_results: A list of newsource objects
    '''
    newsource_results = []
    for news_item in newsource_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')

        newsource_object = Source(id,name,description,url,category,country)
        newsource_results.append(newsource_object)

    return newsource_results

def get_source(source_id,limit):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = article_url.format(source_id,limit,api_key)
    print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
 
        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(source):
    source_articles = []
    for item_article in source:
        author = item_article.get('author')
        title = item_article.get('title')
        description = item_article.get('description')
        url = item_article.get('url')
        urlToImage = item_article.get('urlToImage')
        publishedAt = item_article.get('publishedAt')
        if urlToImage:
            articles_object = Articles(author,title,description,url,urlToImage,publishedAt)
            source_articles.append(articles_object)
    return source_articles
