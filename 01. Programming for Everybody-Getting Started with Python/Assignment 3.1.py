# @Author: Antero Maripuu <machinelearningxl>
# @Date:   2017-11-07T13:45:29+00:00
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignment 3.1.py
# @Last modified by:   Antero Maripuu
# @Last modified time: 2017-11-07T20:50:31+00:00

#3.1 Write a program to prompt the user for hours and rate per hour using
#raw_input to compute gross pay. Award time-and-a-half for the hourly rate for
#all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to
#test the program (the pay should be 498.75). You should use raw_input to read a
#string and float() to convert the string to a number. Do not worry about error
#checking the user input - assume the user types numbers properly.

inp=float(input("Worked Hours: ")) #Phyton 3 function input(), Python 2.7 raw_input()
inp2=float(input("Pay rate: "))

def rate(x, y):
    return x*y

if rate(inp,inp2)<=40:
    print(rate(inp,inp2))
else:
    rate2=inp2 * 40 + ( inp2 * 1.5 * ( inp - 40) )
    print("Pay: ",rate2)
