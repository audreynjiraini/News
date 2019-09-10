from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources
from ..models import Sources

@main.route('/')
def index():
    '''
    View root page that returns the index page and its data
    '''
    
    title = "News Highlight"
    
    sources = get_sources('politics')
    tech_sources = get_sources('technology')
    bus_sources = get_sources('business')
    sports_sources = get_sources('sports')
    ent_sources = get_sources('entertainment')
    
    return render_template('index.html', title = title, sources = sources, tech_sources = tech_sources, bus_sources = bus_sources, sports_sources = sports_sources, ent_sources = ent_sources)


@main.route('/sources/<id>')
def articles(id):
    '''
    View articles page function that returns the article details page and its data
    '''
    
    title = f"{id} Articles"
    
    articles = get_articles(id)
    
    return render_template('articles.html', title = title, articles = articles)