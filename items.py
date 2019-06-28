# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossspiderItem(scrapy.Item):
    name = scrapy.Field()
    highSalary = scrapy.Field()
    lowSalary = scrapy.Field()
    place = scrapy.Field()
    expersion = scrapy.Field()
    education = scrapy.Field()
    fuli = scrapy.Field()
    yaoqiu = scrapy.Field()
