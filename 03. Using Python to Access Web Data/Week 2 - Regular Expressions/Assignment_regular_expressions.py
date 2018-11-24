# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date : 2018-11-23 15:57
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename : Assignment_regular_expressions

"""
In this assignment you will read through and parse a file with text and numbers.
You will extractall the numbers in the file and compute the sum of the numbers.
"""

import re

words_file = input("Type a file name for processing:  ")
if words_file == "":
    words_file = open("regex text data.txt")


su = 0
for x in words_file:
    line = x.strip()
    stuff = re.findall("[0-9]+", x)
    for y in stuff:
        y = int(y)
        su += y

print("Sum of the numbers: ", su)





