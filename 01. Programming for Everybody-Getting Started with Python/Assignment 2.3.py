# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date:   2018-10-19 10:41:51
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera 2018
# @Filename: Assignment 2.3.py
# @Last modified by:   Antero Maripuu Github:<machinelearningxl>
# @Last modified time: 2018-11-16 15:23:38


"""
Write a program to prompt the user for hours and
rate per hour to compute gross pay.
"""

inp = float(input("Please enter your hours: "))  # Python 3 function input(), Python 2.7 raw_input()
inp2 = float(input("Please enter your rate (e.g £20.15): "))


def fname(x,y):
    print(x*y)


print("Your calculated cross pay is "), fname(inp, inp2)


