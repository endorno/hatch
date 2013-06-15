# coding=utf-8
from bottlenose import api
from bs4 import BeautifulSoup
from lxml import etree

AMAZON_ACCESS_KEY_ID="AKIAJSRKJ3SKR7FEZTIQ"
AMAZON_SECRET_KEY="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"
AMAZON_ASSOC_TAG="yukib1028-22"

amazon = api.Amazon(AMAZON_ACCESS_KEY_ID, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, Region="JP")

def item_search(keywords, search_index="Music", item_page=1):
    response = amazon.ItemSearch(SearchIndex=search_index, Keywords=keywords, ItemPage=item_page, ResponseGroup="Images,ItemAttributes")
    #print response
    soup = BeautifulSoup(response)
    return soup.findAll('item')

if __name__ == '__main__':
	print "login"
	for item in item_search('idol master'):
		print item.find('smallimage').text
		title = item.find('title').text
		try:
			author = item.find('author').text
		except:
			author = ""
		asin = item.find('asin').text
		print("%s (%s) - %s" % (title, author, asin))
