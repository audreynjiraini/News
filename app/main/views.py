from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    View root page that returns the index page and its data
    '''
    
    title = "News Highlight"
    
    return render_template('index.html', title = title)


@main.route('/sources/<id>')
def articles(id):
    '''
    View articles page function that returns the article details page and its data
    '''
    
    title = f"{id} Articles"
    
    return render_template('articles.html', title = title)