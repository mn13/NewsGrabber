import feedparser
from abc import ABC, abstractmethod
from newspaper import Article

class News_Graber(ABC):
    @property
    def url(self):
        return self._url
    
    @abstractmethod
    def news(self):
        feed = feedparser.parse(self.url)
        return [
            {
                'title': item['title'],
                'link': item['link'],
                'desc': item['description'],
                'published': item['published']
            }
            for item in feed['items']]

    def grub(self, url):
        article = Article(url, language='ru')
        article.download()
        article.parse()
        return {
            'title': article.title,
            'image': article.top_image,
            'content': [paragraph for paragraph in article.text.split('\n') if paragraph]
        }
            