# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from vinc_crawler.items import VincCrawlerItem ###wu


product_ranking_gl = 1;

class VincCrawlerSpider(CrawlSpider):
    name = "product";
    start_urls = [
        '''https://tw.search.buy.yahoo.com/search/shopping/product;_ylt=AgmNyRaBhCO_B31Ic6x.0MR0cB4J?p=%E5%A5%B3&qt=product&cid=10&clv=2&cid_path=1_7&property=shopping&sub_property=shopping&srch=product&pg=1&sort=-sales&nst=1&act=gdsearch&rescheck=1''',
        '''https://tw.search.buy.yahoo.com/search/shopping/product;_ylt=AgmNyRaBhCO_B31Ic6x.0MR0cB4J?p=%E5%A5%B3&qt=product&cid=10&clv=2&cid_path=1_7&property=shopping&sub_property=shopping&srch=product&pg=2&sort=-sales&nst=1&act=gdsearch&rescheck=1''',
        '''https://tw.search.buy.yahoo.com/search/shopping/product;_ylt=AgmNyRaBhCO_B31Ic6x.0MR0cB4J?p=%E5%A5%B3&qt=product&cid=10&clv=2&cid_path=1_7&property=shopping&sub_property=shopping&srch=product&pg=3&sort=-sales&nst=1&act=gdsearch&rescheck=1''',
    ]


    def parse(self, response):
        global product_ranking_gl
        product_ranking = product_ranking_gl
        for product in response.css('.item .wrap'):
            yield {
                'name':  product.css('.srp-pdtitle a::text').extract(),
                'price': int(product.css('.srp-pdprice ::text').re_first(r'[\d|,]+').replace(",","")),
                'rank':  product_ranking,
            }
            product_ranking += 1
            
        product_ranking_gl = product_ranking;

        
            
