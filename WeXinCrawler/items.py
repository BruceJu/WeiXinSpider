# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import datetime

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


class WeixinItemLoader(ItemLoader):
    # 自定义itemloader
    default_output_processor = TakeFirst()


def format_time(value):
    return datetime.datetime.fromtimestamp(value)

def format_str(value):
    return str(value)


class WexincrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    appmsgid = scrapy.Field(input_processor=MapCompose(format_str))
    cover = scrapy.Field()
    digest = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    update_time = scrapy.Field(input_processor=MapCompose(format_time))

    crawl_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
              insert into weixin_spider(cover, appmsgid, diqest, link, title, update_time) VALUES (%s, %s, %s, %s, %s, %s)
              ON DUPLICATE KEY UPDATE appmsgid=VALUES(appmsgid), link=VALUES(link)
          """
        params = (
            self["cover"], self["appmsgid"], self["digest"], self["link"],
            self["title"], self["update_time"]
        )

        return insert_sql, params



