# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date:   2018-10-19 10:41:51
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignment 7.1.py
# @Last modified by:   Antero Maripuu Github:<machinelearningxl>
# @Last modified time: 2018-11-16 15:30:08


"""
7.1 Write a program that prompts for a file name, then opens that file and
reads through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output below.
You can download the sample data at
"""

words_file = input("Type a file name for processing: ")
if words_file == "":
    words_file = open("words.txt")

for lin in words_file:
    lin = lin.upper().strip()
    print(lin)