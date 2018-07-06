# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item, Field

class ProxyserverspiderItem(Item):
    target = Field()
    IP = Field()
    PORT = Field()
    ProxyType = Field()
    ReqType = Field()
    Loc = Field()
    Delay = Field()
