# coding=utf-8
from bottlenose import api
from bs4 import BeautifulSoup
from lxml import etree


class Amazons(object):

	def __init__(self):
		AMAZON_ACCESS_KEY_ID="AKIAJSRKJ3SKR7FEZTIQ"
		AMAZON_SECRET_KEY="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"
		AMAZON_ASSOC_TAG="yukib1028-22"
		self.amazon = api.Amazon(AMAZON_ACCESS_KEY_ID, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, Region="JP")
		pass

	def item_search(self, keywords, search_index="", item_page=1):
		response = self.amazon.ItemSearch(SearchIndex=search_index, Keywords=keywords, ItemPage=item_page, ResponseGroup="OfferFull")
		#print response
		soup = BeautifulSoup(response)
		print response
		self.create_jsondata(soup.findAll('item'))

	def create_jsondata(self, response):
		for item in response:
			smallimage = item.find('smallimage').text
			asin = item.find('asin').text
			title = item.find('title').text
			price = item.find('FormattedPrice').text
			print("%s (%s) - %s / %s" % (title, price, smallimage, asin))

if __name__ == '__main__':
	amazon = Amazons()
	amazon.item_search('idol master', 'Music')
