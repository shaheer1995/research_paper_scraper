# -*- coding: utf-8 -*-
import scrapy
from ..items import ResearchPapersItem


class ResearchPaperSpider(scrapy.Spider):
    name = 'papers'
    page_number = 2
    start_urls = [
        'https://paperswithcode.com/'
        ]

    def parse(self, response):
        
        items = ResearchPapersItem()
        blocks = response.css('div.item')

        for block in blocks:
            paper_title = block.css('h1 a::text').extract()
            date_published = block.css('.author-name-text').css('::text').extract()
            tags = block.css('.badge-primary::text').extract()
            description = block.css('.item-strip-abstract').css('::text').extract()
            stars = block.css('.badge-secondary::text').extract()
            paper_link = block.css('h1 a').xpath("@href").extract()
        
            items['paper_title'] = paper_title
            items['date_published'] = date_published
            items['tags'] = tags
            items['description'] = description
            items['stars'] = stars
            items['paper_link'] = paper_link

            yield items

        next_page = 'https://paperswithcode.com/?page='+str(ResearchPaperSpider.page_number)
        if ResearchPaperSpider.page_number <= 1000:
            ResearchPaperSpider.page_number += 1
            yield response.follow(next_page,callback = self.parse)



