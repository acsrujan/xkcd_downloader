# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline



class XKCDImagesPipeline(ImagesPipeline):
    
    def image_key(self, url):

        image_name = re.match(".+/(?P<name>.+.jpg|.jpeg|.gif|.png$)", url)

        return '%s' % (image_name.group("name"))


    def get_media_requests(self, item, info):

        if self.__class__ not in info.spider.pipeline:
            return

        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)


