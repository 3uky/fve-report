import scrapy
from datetime import date


class OteSpider(scrapy.Spider):
    name = "ote"
    allowed_domains = ["ote-cr.cz"]
    start_urls = [f"https://www.ote-cr.cz/cs/kratkodobe-trhy/elektrina/denni-trh?date={date.today()}"]

    def parse(self, response):
        for row in response.xpath('//*[@class="table report_table"]//tbody/tr'):
            if row.xpath('th[1]//text()').extract_first():
                hour = int(row.xpath('th[1]//text()').extract_first())
                price = float(row.xpath('td[1]//text()').extract_first().strip().replace(',','.'))
                yield {
                    'hour': hour,
                    'price': price
                }
        print (date.today())