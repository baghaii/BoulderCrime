# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field 


class CallLogItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	case = Field()
	date = Field()
	time = Field()
	loc = Field()
	call_type = Field()
