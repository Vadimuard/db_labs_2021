from scrapy import cmdline


def crawl_repka():
    cmdline.execute("scrapy crawl repka".split())
