#!/usr/bin/python3

from bs4 import BeautifulSoup

with open("blog-feed.xml", "r") as f:
    
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    root = soup.item
    
    root_childs = [e.name for e in root.descendants if e.name is not None]
    print(root_childs)
