# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date : 2018-11-25 00:27
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename : Assignment_XML.py

"""
EXTRACTING DATA FROM XML
In this assignment you will write a Python program somewhat similar to
http://www.pythonlearn.com/code/geoxml.py. The program will prompt for a URL,
read the XML data from that URL using urllib and then parse and extract the
comment counts from the XML data, compute the sum of the numbers in the file.
We provide two files for this assignment. One is a sample file where we give you
the sum for your testing and the other is the actual data you need to process for
the assignment.
    Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
    Actual data: http://python-data.dr-chuck.net/comments_277461.xml
You do not need to save these files to your folder since your program will read
the data directly from the URL. Note: Each student will have a distinct data url
for the assignment - so only use your own data url for analysis.
DATA FORMAT AND APPROACH
The data consists of a number of names and comment counts in XML as follows:
<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>
You are to look through all the <comment> tags and find the <count> values sum
the numbers. The closest sample code that shows how to parse XML is geoxml.py.
But since the nesting of the elements in our data is different than the data we
are parsing in that sample code you will have to make real changes to the code.
To make the code a little simpler, you can use an XPath selector string to look
through the entire tree of XML for any tag named 'count' with the following line
of code:
counts = tree.findall('.//count')
Take a look at the Python ElementTree documentation and look for the supported
XPath syntax for details. You could also work from the top of the XML down to
the comments node and then loop through the child nodes of the comments node.

We'll left XPath for another moment, as it requires further investigation. For
now we'll look for the count tags by knowing its structure:
commentinfo -> comments -> comment -> count

"""

import urllib.request, urllib.request
import xml.etree.ElementTree as ET

url = input('Enter XML URL - ')
if url == "":
    url = "http://python-data.dr-chuck.net/comments_277465.xml"

open_url = urllib.request.urlopen(url).read()

stuff = ET.fromstring(open_url)
lst = stuff.findall("comments/comment")

count = 0

for item in lst:
    count += int(item.find("count").text)
print("Total count: ", count)


