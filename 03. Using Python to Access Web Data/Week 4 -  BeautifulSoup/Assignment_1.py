# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date : 2018-11-24 23:42
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename : Assignment_1.py


"""
This assignment consists of using urllib to read the HTML from the data files
indicated, and parse the data, extract the numbers and compute the sum of the
numbers in the file

view-source: http://python-data.dr-chuck.net/comments_46.html

DATA FORMAT:
 The file is a table of names and comment counts. You can ignore most of the data
 in the file except for lines like the following:

<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

You are to find all the <span> tags in the file and pull out the numbers from the
tag and sum the numbers.

Look at the sample code (http://www.pythonlearn.com/code/urllink2.py) provided.

It shows how to find all of a certain kind of tag, loop through the tags and extract
the various aspects of the tags.
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs
You need to adjust this code to look for span tags and pull out the text content of the
span tag, convert them to integers and add them up to complete the assignment.
"""

import urllib.request, urllib.response, urllib.request
from bs4 import *  # BeautifulSoup

sum = 0
url = input('Enter URL - ')
if url == "":
    url = "http://python-data.dr-chuck.net/comments_46.html"

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    sum += int(tag.contents[0])

"""
First contents[0] gives the HTML tag, the second one, gives  the head tag. 
The third one leads to the title tag, and the fourth one gives you the actual content.
"""

print("The sum of the numbers in the file", sum)
