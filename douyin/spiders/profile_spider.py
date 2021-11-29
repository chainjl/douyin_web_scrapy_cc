import scrapy
from scrapy_splash import SplashRequest
from douyin.items import DouyinImageItem

class ProfileSpiderSpider(scrapy.Spider):
    name = 'profile_spider'
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
        url = 'https://www.douyin.com/user/MS4wLjABAAAA00nKo5lh2WLrvyxx1niCYdDN7U78e8WlaYQFhoLcXvQ'

        yield SplashRequest(url, self.parse, endpoint='execute', args={'lua_source': self.script})

    def parse(self, response):
        images = response.xpath("//*[contains(@class, '_97a0a8fa4fb9eb092882c832463dad24-scss')]/img/@src").extract()

        image_urls = ['https:' + image for image in images]

        item = DouyinImageItem()
        item['image_urls'] = image_urls
        yield item

