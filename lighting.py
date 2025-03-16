import scrapy
class LightingSpider(scrapy.Spider):
    name = 'lighting'
    allowed_domains = ['https://divan.ru/sankt-peterburg/']
    start_urls = ['https://www.divan.ru/sankt-peterburg/category/svet']
    def parse(self, response):
        # Находим все элементы с источниками освещения
        for product in response.css('.product-item'):
            yield {
                'name': product.css('.product-title::text').get(),
                'price': product.css('.product-price::text').get(),
                'link': response.urljoin(product.css('a::attr(href)').get()),
            }
        # Пагинация: переходим на следующую страницу, если она есть
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

