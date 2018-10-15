from News_Graber import News_Graber

class Lenta(News_Graber):
    def __init__(self):
        self._url = 'http://lenta.ru/rss'

    def news(self, limit = None):
        if limit is None:
            return super.news()
        elif limit > 0:
            return super().news()[0:limit]
        return []