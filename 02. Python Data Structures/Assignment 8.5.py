# @Author: Antero Maripuu
# @Date:   2017-11-07T15:03:35+00:00
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignmenet 8.5.py
# @Last modified by:   Antero Maripuu Github:<machinelearningxl>
# @Last modified time: 2018-11-16 15:52:59

"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line
(i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
"""
'''
Desired Output:
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu
rjlowe@iupui.edu
zqian@umich.edu
rjlowe@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
gsilver@umich.edu
gsilver@umich.edu
zqian@umich.edu
gsilver@umich.edu
wagnermr@iupui.edu
zqian@umich.edu
antranig@caret.cam.ac.uk
gopal.ramasammycook@gmail.com
david.horwitz@uct.ac.za
david.horwitz@uct.ac.za
david.horwitz@uct.ac.za
david.horwitz@uct.ac.za
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
louis@media.berkeley.edu
ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
'''


words_file = input("Type a file name for processing: ")
if words_file == "":
    words_file = open("mbox-short.txt")
count = 0
for x in words_file:
    x = x.strip()
    if x.startswith("From "):
        words = x.split()
        print(words[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")