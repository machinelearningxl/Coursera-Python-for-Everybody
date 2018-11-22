# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date:   2018-10-19 10:41:51
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignment 10.2.py
# @Last modified by:   Antero Maripuu Github:<machinelearningxl>
# @Last modified time: 2018-11-16 15:53:49


"""
10.2 Write a program to read through the mbox-short.txt and figure out the
distribution by hour of the day for each of the messages. You can pull the
hour out from the 'From ' line by finding the time and then splitting the
string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below. Note that the autograder does not have support
for the sorted() function.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

Desired Output:
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

"""
counts = dict()

words_file = input("Type a file name for processing: ")
if words_file == "":
    words_file = open("mbox-short.txt")

for words in words_file:
    if words.startswith("From "):
            words = words.split()[5]
            split = words.split(":")[0]
            counts[split] = counts.get(split, 0) + 1
#  print(counts)

lst = list()
for key, val in counts.items():
    lst.append((key, val))
lst.sort(reverse=False)
for val, key in lst[:]:
    print(val, key)


