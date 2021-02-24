from lxml import etree


def xslt_parse():
    dom = etree.parse('results/repka.xml')
    xslt = etree.parse('repka.xslt')
    transform = etree.XSLT(xslt)
    new_dom = transform(dom)
    with open('results/repka.html', 'wb') as f:
        f.write(etree.tostring(new_dom, pretty_print=True))
