from News_Graber import News_Graber

class m24(News_Graber):
    def __init__(self):
        self._url = 'http://www.m24.ru/rss.xml'

    def news(self, limit = None):
        if limit is None:
            return super.news()
        elif limit > 0:
            return super().news()[0:limit]
        return []