from datetime import datetime

import pytz
import scrapy

EGLOOS_ID = "oniondev"
BLOG_URL = f"http://{EGLOOS_ID}.egloos.com"

class EgloosBlogSpider(scrapy.Spider):
    name = 'egloos_blogspider'
    start_urls = ['http://oniondev.egloos.com']

    def parse(self, response, **kwargs):
        # title_xpath_4th = '//*[@id="section_content"]/div/div[4]/div[1]/div/h2/a'
        # content_xpath_4th = '//*[@id="section_content"]/div/div[4]/div[2]/div/div'
        # created_xpath = '//*[@id="section_content"]/div/div[1]/div[1]/ul/li[2]/abbr'

        posts = response.xpath('//*[@id="section_content"]/div/div')
        for post in posts:
            title = "".join(post.xpath('./div[1]/div/h2/a/text()').extract())
            content = "\n".join(post.xpath('./div[2]/div').css('*::text').getall())
            created_str = post.xpath('./div[1]/ul/li[2]/abbr/text()').get()
            created_dt = datetime.strptime(created_str,"%Y/%m/%d %H:%M").replace(tzinfo=pytz.timezone('Asia/Seoul'))
            print("created_dt:", created_dt)

            if not title or not content:
                continue

            yield {
                'title': title,
                'content': content,
                'created': str(created_dt)
            }

        # pages = response.xpath('//*[@id="section_content"]/div/div[6]/span/a')
        # for page in pages:
        #     relative_path = page.xpath('./@href').get()  # (ex) /page/3
        #     yield response.follow(f"{BLOG_URL}{relative_path}", self.parse)

