import feedparser
from abc import ABC, abstractmethod
from newspaper import Article

class News_Grabber(ABC):
    @property
    def url(self):
        return self._url
    
    def news(self, limit = None):
        feed = feedparser.parse(self.url)
        res = [
            {
                'title': item['title'],
                'link': item['link'],
                'desc': item['description'],
                'published': item['published']
            }
            for item in feed['items']]
        if limit is None:
            return res
        elif limit > 0:
            return res[0:limit]
        return []

    def grub(self, url):
        article = Article(url, language='ru')
        article.download()
        article.parse()
        return {
            'title': article.title,
            'image': article.top_image,
            'content': [paragraph for paragraph in article.text.split('\n') if paragraph]
        }
            