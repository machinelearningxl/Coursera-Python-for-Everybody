# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date:   2018-10-19 10:41:51
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignment 2.5.py
# @Last modified by:   Antero Maripuu Github:<machinelearningxl>


"""
2.5 Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted
temperature.
"""

inp = (input("Please enter a Celsius temperature "))  # Python 3 function input(), Python 2.7 raw_input()


def fname(x):
    return x * (9.0/5.0) + 32


print("Temperature in Fahrenheit", fname(inp))
