# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date:   2018-10-19 10:41:51
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignment 8.4.py
# @Last modified by:   Antero Maripuu Github:<machinelearningxl>
# @Last modified time: 2018-11-16 15:51:43


"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the
line into a list of words using the split() function. The program should build
a list of words. For each word on each line check to see if the word is already
in the list and if not append it to the list. When the program completes, sort
and print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

Desired Output:
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
"""


def list_of_words(values):
    lists = []
    for d in words_file:
        for c in d.split():
            lists.append(c)
    return lists


def sort_and_uniqe(values):
    lista = []
    for x in values:
        if x not in lista:
            lista.append(x)
            lista.sort()
    return lista


words_file = input("Type a file name for processing: ")
if words_file == "":
    words_file = open("romeo.txt")

x = list_of_words(words_file)
print(sort_and_uniqe(x))










