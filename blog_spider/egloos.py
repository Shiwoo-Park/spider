import scrapy


class EgloosBlogSpider(scrapy.Spider):
    name = 'egloos_blogspider'
    start_urls = ['https://oniondev.egloos.com']

    def parse(self, response, **kwargs):
        for quote in response.css('div.post_view'):
            yield {
                'title': quote.css('h2.entry-title').get(),
                'text': quote.css('div.hentry').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

