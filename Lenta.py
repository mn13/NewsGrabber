from News_Grabber import News_Grabber

class Lenta(News_Grabber):
    def __init__(self):
        self._url = 'http://lenta.ru/rss'