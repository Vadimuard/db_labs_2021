from scrapy import cmdline


def crawl_ukrnet():
    cmdline.execute("scrapy crawl ukr.net".split())
