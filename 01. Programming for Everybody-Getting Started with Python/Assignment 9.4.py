# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date:   2018-10-19 10:41:51
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignment 9.4.py
# @Last modified by:   Antero Maripuu Github:<machinelearningxl>
# @Last modified time: 2018-11-16 15:53:20


"""
9.4 Write a program to read through the mbox-short.txt and figure out who has
the most commits. The program looks for 'From ' lines and takes the second word
of those lines as the person who sent the mail. The program creates a Python
dictionary that maps the senders mail address to a count of the number of
times they appear in the file. After the dictionary is produced, the program
reads through the dictionary using a maximum loop to find the most prolific
committer.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

Desired Output:
cwen@iupui.edu 5

"""