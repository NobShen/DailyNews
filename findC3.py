#!//usr/bin/python3

from bs4 import BeautifulSoup
import bs4
import requests as req

with req.get("https://nhombancongnhan.com/blog-feed.xml") as f:
	soup = BeautifulSoup(f.text, 'html.parser')
	# for tag in soup.findAll('item'):
	print(soup.item)
#		print(tag)
