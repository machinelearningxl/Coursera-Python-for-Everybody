# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date:   2018-10-19 10:41:51
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignment 5.2.py
# @Last modified by:   Antero Maripuu Github:<machinelearningxl>
# @Last modified time: 2018-11-16 15:25:25


"""
5.2 Write a program that repeatedly prompts a user for integer numbers until
the user enters 'done'. Once 'done' is entered, print out the largest and
smallest of the numbers. If the user enters anything other than a valid number
catch it with a try/except and put out an appropriate message and ignore the
number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown.
"""

empty_list = []

def minimum(values):
    smallest = None
    for value in values:
        if smallest is None:  # TRUE only first time, after it always false
            smallest = value
        elif value < smallest:
            smallest = value
    return smallest


def maximum(values):
    max = None
    for value in values:
        if max is None:  # TRUE only first time, after it always false
            max = value
        elif value > max:
            max = value
    return max


while True:
    number = input("Enter a number e.g 5.5 ")

    if number == "done":
        break

    try:
        number = int(number)

    except:
        continue

    empty_list.append(number)

print("Smallest value", minimum(empty_list))
print("Maximum value ", maximum(empty_list))
