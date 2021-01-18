import logging
from datetime import datetime

import pytz
import scrapy


class EgloosBlogSpider(scrapy.Spider):
    '''
    <Usage>
    scrapy runspider egloos.py -a user_id=oniondev -o egloos_oniondev.json
    '''
    name = 'egloos_blogspider'
    blog_url = None
    start_urls = []

    def __init__(self, user_id=None, *args, **kwargs):
        super().__init__()
        self.blog_url = f"http://{user_id}.egloos.com"
        self.start_urls = [self.blog_url]

    def parse(self, response, **kwargs):
        posts = response.xpath('//*[@id="section_content"]/div/div')
        for post in posts:
            title = "".join(post.xpath('./div[1]/div/h2/a/text()').extract())
            content = "\n".join(post.xpath('./div[2]/div').css('*::text').getall())
            created_str = post.xpath('./div[1]/ul/li[2]/abbr/text()').get()
            try:
                created_dt = datetime.strptime(created_str, "%Y/%m/%d %H:%M").replace(
                    second=0,
                    tzinfo=pytz.timezone('Asia/Seoul')
                )
                created_str = created_dt.strftime("%Y-%m-%d %H:%M:%S")
            except Exception:
                logging.error(f"Date parse failed: {created_str}")

            if not title or not content:
                continue

            yield {
                'title': title,
                'content': content,
                'created': created_str,
            }

        pages = response.xpath('//*[@id="section_content"]/div/div[6]/span/a')
        for page in pages:
            relative_path = page.xpath('./@href').get()  # (ex) /page/3
            yield response.follow(f"{self.blog_url}{relative_path}", self.parse)
