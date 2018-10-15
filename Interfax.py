from News_Grabber import News_Grabber

class Interfax(News_Grabber):
    def __init__(self):
        self._url = 'http://www.interfax.ru/rss.asp'

    def news(self, limit = None):
        if limit is None:
            return super.news()
        elif limit > 0:
            return super().news()[0:limit]
        return []