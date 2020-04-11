# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ResearchPapersItem(scrapy.Item):
    paper_title = scrapy.Field()
    date_published = scrapy.Field()
    description = scrapy.Field()
    tags = scrapy.Field()
    stars = scrapy.Field()
    paper_link = scrapy.Field()
    
    pass
