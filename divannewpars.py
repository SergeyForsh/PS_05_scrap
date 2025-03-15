import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru/sankt-peterburg/"]
    start_urls = ["https://www.divan.ru/sankt-peterburg/category/svet"]

    def parse(self, response):
        divans = response.css('div.WdR1o')
        for divan in divans:
            yield {
                'name' : divan.css('div.ui-GPFV8 span::text').get(),
                'price' : divan.css('div.ui-LD-ZU KIkOH span::text').get(),
                'url' : divan.css('a').attrib["href"]
            }
