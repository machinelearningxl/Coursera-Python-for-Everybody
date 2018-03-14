# @Author: Antero Maripuu <machinelearningxl>
# @Date:   2017-10-26T16:51:22+01:00
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignment 2.5.py
# @Last modified by:   Antero Maripuu
# @Last modified time: 2017-11-07T19:38:28+00:00

#2.5 Write a program which prompts the user for a Celsius temperature,
#convert the temperature to Fahrenheit, and print out the converted
#temperature.

inp=float(input("Please enter a Celsius temperature ")) #Phyton 3 function input(), Python 2.7 raw_input()

def fname(x):
    return x * (9.0/5.0) + 32

print("Temperature in Fahrenheit", fname(inp))
