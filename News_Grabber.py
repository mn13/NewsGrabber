import feedparser
from newspaper import Article

class News_Grabber():

    source ={ 
        'interfax':'http://www.interfax.ru/rss.asp',
        'lenta':'http://lenta.ru/rss',
        'kommersant':'http://www.kommersant.ru/RSS/news.xml',
        'm24':'http://www.m24.ru/rss.xml'
    }
    
    def setNewUrl(self, url, name):
        self.source[name] = url

    def get(self, source, limit = None):
        # exception
        feed = feedparser.parse(self.source.get(source))
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
            