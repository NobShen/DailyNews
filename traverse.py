#!/usr/bin/python3

from bs4 import BeautifulSoup

with open("blog-feed.xml", "r") as f:
    
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
            
    for child in soup.recursiveChildGenerator():
        
        if child.name:
            
            print(child.name)
