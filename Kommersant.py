from News_Grabber import News_Grabber

class Kommersant(News_Grabber):
    def __init__(self):
        self._url = 'http://www.kommersant.ru/RSS/news.xml'

    def news(self, limit = None):
        if limit is None:
            return super.news()
        elif limit > 0:
            return super().news()[0:limit]
        return []