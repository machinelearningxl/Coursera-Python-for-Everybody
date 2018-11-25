# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date : 2018-11-24 21:34
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename : urllinks.py

import urllib
from bs4 import *  # BeautifulSoup

url = input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))



