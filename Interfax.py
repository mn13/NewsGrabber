from News_Grabber import News_Grabber

class Interfax(News_Grabber):
    def __init__(self):
        self._url = 'http://www.interfax.ru/rss.asp'