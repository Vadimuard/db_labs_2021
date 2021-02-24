from lxml import etree


def analyze_ukrnet_data():
    root = None
    with open('results/ukr_net.xml', 'r') as file:
        root = etree.parse(file)

    pagesCount = root.xpath('count(//page)')
    textFragmentsCount = root.xpath('count(//fragment[@type="text"])')
    f = open("results/task2.txt", "w")
    f.write(
        f'Average number of text fragments per page {textFragmentsCount / pagesCount}')
    f.close()
