import os

class Config:
    '''
    General configuration parent class
    '''
    
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey=83d6ba2c0cf74071ab06432e21125afb'
    
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=amazon&language=en&apiKey=83d6ba2c0cf74071ab06432e21125afb'
    
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
    @staticmethod
    def init_app(app):
        pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}