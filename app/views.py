from flask import render_template
from app import app
from .requests import get_sources

# Views
@app.route('/')
def index():
    
    sports = get_sources('sports')
    entertainment = get_sources('entertainment')
    technology = get_sources('technology')
    headlines = get_headlines('10')
    business = get_sources('business')
    general = get_sources('general')
    title = 'Newshighlights'
    return render_template('index.html', title = title, sports =sports, entertainment=entertainment, technology=technology, headlines=headlines, business=business, general=general)

@app.route('/newspage/<int:newspage_id>')
def newspage(newspage_id):

    '''
    View news page function that returns the newspage details page and its data
    '''
    return render_template('articles.html',id = newspage_id)