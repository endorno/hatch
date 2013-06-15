# coding=utf-8
from bottlenose import api
from bs4 import BeautifulSoup
from lxml import etree


class Amazons(object):
    def __init__(self):
        AMAZON_ACCESS_KEY_ID = "AKIAJSRKJ3SKR7FEZTIQ"
        AMAZON_SECRET_KEY = "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"
        AMAZON_ASSOC_TAG = "yukib1028-22"
        self.amazon = api.Amazon(AMAZON_ACCESS_KEY_ID, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, Region="JP")
        pass

    def item_search(self, keywords, search_index="", item_page=1):
        response = self.amazon.ItemSearch(SearchIndex=search_index, Keywords=keywords, ItemPage=item_page,
                                          ResponseGroup="OfferFull,Images,ItemAttributes")
        soup = BeautifulSoup(response)
        return self.create_jsondata(soup.findAll('item'))

    def create_jsondata(self, items_xml):
        ret = []
        for item in items_xml:
            thumbnail=""
            detail_link = ""
            title = ""
            price = 0
            asin = 0
            try:
                thumbnail = item.find('mediumimage').find("url").text
            except:
                pass
            try:
                detail_link = item.find('detailpageurl').text
            except:
                pass
            try:
                title = item.find("title").text
            except:
                pass
            try:
                price = int(item.find('price').find('amount').text)
            except:
                pass
            try:
                asin = item.find("asin").text
            except:
                pass
            item = {"title":title,"price":price,"thumbnail":thumbnail,"asin":asin,"detail_link":detail_link}
            ret.append(item)
        return ret
from prettyprint import pp
if __name__ == '__main__':
    amazon = Amazons()
    pp(amazon.item_search(u'ギター', 'All'))
