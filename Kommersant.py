from News_Grabber import News_Grabber

class Kommersant(News_Grabber):
    def __init__(self):
        self._url = 'http://www.kommersant.ru/RSS/news.xml'