from lxml import etree


class UkrNetPipeline:
    def open_spider(self, spider):
        self.root = etree.Element('data')

    def close_spider(self, spider):
        with open('results/ukr_net.xml', 'wb') as f:
            etree.ElementTree(self.root).write(f, pretty_print=True, encoding="UTF-8")

    def process_item(self, item, spider):
        page = etree.SubElement(self.root, 'page', url=item['url'])
        for txt in item['fragment_text']:
            etree.SubElement(page, 'fragment', type='text').text = txt
        for img in item['fragment_img']:
            etree.SubElement(page, 'fragment', type='image').text = img
        return item


class RepkaPipeline:
    def open_spider(self, spider):
        pass
        # self.root = etree.Element('data')

    def close_spider(self, spider):
        pass
        # with open('results/ukr_net.xml', 'wb') as f:
        #     etree.ElementTree(self.root).write(f, pretty_print=True, encoding="UTF-8")

    def process_item(self, item, spider):
        # page = etree.SubElement(self.root, 'page', url=item['url'])
        # for txt in item['fragment_text']:
        #     etree.SubElement(page, 'fragment', type='text').text = txt
        # for img in item['fragment_img']:
        #     etree.SubElement(page, 'fragment', type='image').text = img
        return item