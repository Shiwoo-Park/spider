import scrapy

class EgloosBlogSpider(scrapy.Spider):
    name = 'egloos_blogspider'
    start_urls = ['https://oniondev.egloos.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)