# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
import string
import random


class DouyinPipeline:
    def process_item(self, item, spider):
        return item

class DouyinDownloadVideoPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        file_name: str = ''.join(random.choice(string.ascii_letters) for i in range(15)) + '.mp4'
        return file_name
