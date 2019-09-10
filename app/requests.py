import urllib.request, json
from .models import Sources

api_key = None

base_url = None

def configure_request(app):
    global api_key, base_url
    
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    
    
def get_sources():
	'''
	Function that gets the json response to url request
	'''
 
	get_sources_url = base_url.format(api_key)

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)

		news_results = None

		if get_sources_response['results']:
			sources_results_list = get_sources_response['results']
			sources_results = process_results(sources_results_list)

	return news_results


def process_sources(sources_list):
	'''
	Function that processes the news sources results and turns it into a list of objects
	Args:
		sources_list: A list of dictionaries that contain sources details
	Returns:
		sources_results: A list of sources objects
	'''
 
	sources_results = []

	for source_item in sources_list:
		id = source_item.get('id') 
		name = source_item.get('name')
		description = source_item.get('description')
		url = source_item.get('url')
		category = source_item.get('category')
		language = source_item.get('language')
		country = source_item.get('country')


		sources_object = Sources(id,name,description,url,category,country,language)
		sources_results.append(sources_object)


	return sources_results


def get_articles(id):
	'''
	Function that processes the articles and returns a list of articles objects
	'''
 
	get_articles_url = articles_url.format(id,api_key)

	with urllib.request.urlopen(get_articles_url) as url:
		articles_results = json.loads(url.read())


		articles_object = None
		if articles_results['articles']:
			articles_object = process_articles(articles_results['articles'])

	return articles_object


def process_articles(articles_list):
	'''
    Function that processes the articles results and turns it into a list of objects
	Args:
		articles_list: A list of dictionaries that contain articles details
	Returns:
		articles_results: A list of articles objects
    '''
    
	articles_object = []
 
	for article_item in articles_list:
		id = article_item.get('id')
		author = article_item.get('author')
		title = article_item.get('title')
		description = article_item.get('description')
		url = article_item.get('url')
		image = article_item.get('urlToImage')
		date = article_item.get('publishedAt')
		
		if image:
			articles_result = Articles(id,author,title,description,url,image,date)
			articles_object.append(articles_result)	

	return articles_object