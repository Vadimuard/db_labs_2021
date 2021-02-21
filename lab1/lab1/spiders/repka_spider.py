import scrapy
from scrapy.selector import Selector
import html5lib
from lab1.items import RepkaItem


class UkrNetSpider(scrapy.Spider):
    name = "repka"
    custom_settings = {
        'ITEM_PIPELINES': {
            'lab1.pipelines.RepkaPipeline': 300,
        }
    }
    allowed_domains = ["repka.ua"]
    start_urls = [
        "https://repka.ua/products/operativnaja-pamjat/",
        "https://repka.ua/products/televizory/",
        "https://repka.ua/products/noutbuki/",

    ]
    selectors = {
        'product-name': "////div[@class='product-name']/a/text()",
        'product-link': "//div[@class='product-name']/a/@href",
        'product-price': "//span[@class='price']/text()",
        'product-image': "//img[@class='product-image-photo']/@src"
    }

    @staticmethod
    def is_str_empty(s):
        return len(s) > 0

    def parse(self, response):
        correct_html = html5lib.serialize(html5lib.parse(response.body))
        selector = Selector(text=correct_html)
        links = selector.xpath(self.selectors['product-link']).extract()[:20]
        print(len(links))
        # for link in links:
        #     item = RozetkaItem()
        #     name = selector.xpath(self.selectors['product-name']).extract()
        #     price = selector.xpath(self.selectors['product-price']).extract()
        #     image = selector.xpath(self.selectors['product-image']).extract()
        #     if image.startswith('//'):
        #         image = image.split('//')[1]
