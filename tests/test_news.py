import unittest
from app.models import Sources,Articles

class SourcesTest(unittest.TestCase):
    '''
    Test behaviour of Sources class
    '''
    
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('bbc-sport','BBC Sport','The home of BBC Sport online. Includes live sports coverage, breaking news, results, video, audio and analysis on Football, F1, Cricket, Rugby Union, Rugby League, Golf, Tennis and all the main world sports, plus major events such as the Olympic Games.','http://www.bbc.co.uk/sport','sports','en','gb')
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))
        

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'bbc-sport')
        self.assertEquals(self.new_source.name,'BBC Sport')
        self.assertEquals(self.new_source.description,'The home of BBC Sport online. Includes live sports coverage, breaking news, results, video, audio and analysis on Football, F1, Cricket, Rugby Union, Rugby League, Golf, Tennis and all the main world sports, plus major events such as the Olympic Games.')
        self.assertEquals(self.new_source.url,'http://www.bbc.co.uk/sport')
        self.assertEquals(self.new_source.category,'sports')
        self.assertEquals(self.new_source.country,'gb')
        self.assertEquals(self.new_source.language,'en')



class ArticlesTest(unittest.TestCase):
    '''
    Test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        self.new_article = Articles('wired','Matt Simon','Amazon Fires and the Horrifying Science of Deforestation','At the core of Brazil\'s out-of-control fires in the Amazon is deforestation. Here\'s how human meddling fundamentally transforms a rainforest.','https://www.wired.com/story/the-horrifying-science-of-the-deforestation-fueling-amazon-fires/','https://media.wired.com/photos/5d6027925af21f000859fc13/191:100/pass/Science_AmazonASAP_1125307709.jpg','2019-08-23T20:50:37Z')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))


    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'wired')
        self.assertEquals(self.new_article.author,'Matt Simon')
        self.assertEquals(self.new_article.title,'Amazon Fires and the Horrifying Science of Deforestation')
        self.assertEquals(self.new_article.description,'At the core of Brazil\'s out-of-control fires in the Amazon is deforestation. Here\'s how human meddling fundamentally transforms a rainforest.')
        self.assertEquals(self.new_article.url,'https://www.wired.com/story/the-horrifying-science-of-the-deforestation-fueling-amazon-fires/')
        self.assertEquals(self.new_article.image,'https://media.wired.com/photos/5d6027925af21f000859fc13/191:100/pass/Science_AmazonASAP_1125307709.jpg')
        self.assertEquals(self.new_article.date,'2019-08-23T20:50:37Z')