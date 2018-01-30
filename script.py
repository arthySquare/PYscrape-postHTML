import urllib2
from bs4 import BeautifulSoup

#quote then query html
quote_page = 'https://coinmarketcap.com/'
page = urllib2.urlopen(quote_page)
#parse
soup = BeautifulSoup(page, 'html.parser')

for x in xrange(100):
	name_box = soup.find('td')

	name = name_box.text.strip()

	print name
