from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'News Highlight'
    return render_template('index.html',message = message)

@app.route('/newspage/<int:newspage_id>')
def newspage(newspage_id):

    '''
    View news page function that returns the newspage details page and its data
    '''
    return render_template('articles.html',id = newspage_id)