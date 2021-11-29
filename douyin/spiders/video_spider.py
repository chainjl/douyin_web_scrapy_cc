import scrapy
from scrapy_splash import SplashRequest
from douyin.items import DouyinVideoItem
import requests
import json

class VideoSpiderSpider(scrapy.Spider):
    name = 'video_spider'
    allowed_domains = ['douyin.com']
    start_urls = ['http://douyin.com/']

    script = '''
        function main(splash, args)
              splash.private_mode_enabled = false
              assert(splash:go(args.url))
              
              assert(splash:wait(0.5))
              
              return {
                html = splash:html()
              }
        end
    '''

    def start_requests(self):
        url = 'https://www.douyin.com/video/7030325108958825735'

        yield SplashRequest(url, self.parse, endpoint='execute', args={'lua_source': self.script})

    def parse(self, response):
        json_string = requests.utils.unquote(response.xpath('//*[@id="RENDER_DATA"]/text()').extract_first())
        json_object = json.loads(json_string)


        video_url = 'https:' + json_object['C_20']['aweme']['detail']['video']['playAddr'][0]['src']

        item = DouyinVideoItem()
        item['file_urls'] = [video_url]

        yield item
