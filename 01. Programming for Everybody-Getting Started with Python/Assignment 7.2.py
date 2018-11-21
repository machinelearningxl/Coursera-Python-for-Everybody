# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date:   2018-10-19 10:41:51
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignment 7.2.py
# @Last modified by:   Antero Maripuu Github:<machinelearningxl>
# @Last modified time: 2018-11-16 15:30:17


"""
7.2 Write a program that prompts for a file name, then opens that file and reads
through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.

Desired Output:
Average spam confidence: 0.750718518519
"""
words_file = input("Type a file name for processing: ")
if words_file == "":
    words_file = open("mbox-short.txt")


def find_extract_values(values):
    count = 0
    sum = 0
    lists = []
    for lin in values:
        lin = lin.rstrip()
        if lin.startswith("X-DSPAM-Confiden"):
            count = count+1
            lists.append(float(lin[19:]))
    for num in lists:
        sum += num

    #  print("Total number of lines ", count)
    print("Average spam confidence: ", sum/count)


find_extract_values(words_file)
