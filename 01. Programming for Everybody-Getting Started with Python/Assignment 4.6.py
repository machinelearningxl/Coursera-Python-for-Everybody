# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date:   2018-10-19 10:41:51
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignment 4.6.py
# @Last modified by:   Antero Maripuu Github:<machinelearningxl>
# @Last modified time: 2018-11-16 15:24:51

"""
#4.6 Write a program to prompt the user for hours and rate per hour using
#raw_input to compute gross pay. Award time-and-a-half for the hourly rate for
#all hours worked above 40 hours. Put the logic to do the computation of
#time-and-a-half in a function called computepay() and use the function to do
#the computation. The function should return a value. Use 45 hours and a rate
#of 10.50 per hour to test the program (the pay should be 498.75). You should
#use raw_input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input unless you want to - you can
assume the user types numbers properly.
"""

hours = float(input("Worked Hours: "))  # Python 3 function input(), Python 2.7 raw_input()
rate = float(input("Pay rate: "))


def computepay(hours, rate):
    if hours <=40:
        return hours*rate
    else:
        return rate * 40 + (rate * 1.5 * (hours - 40))


print(computepay(45, 10.5))