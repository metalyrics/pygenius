import scrapy
from ..utils import process_lyrics

class GeniusSpider(scrapy.Spider):
    name = 'genius'
    custom_settings = { 
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
    start_urls = ['https://genius.com/{}'.format(self.song_path)]

    def parse(self, response):
        return scrapy.Request(url = response.url, callback = self.parse_lyrics_page)

    def parse_lyrics_page(self, response):
        lyrics = response.xpath('//div[@class="lyrics"]//text()').getall()
        return { 'lyrics': process_lyrics(''.join(lyrics)) }