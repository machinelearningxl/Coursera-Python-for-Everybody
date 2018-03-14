# @Author: Antero Maripuu <machinelearningxl>
# @Date:   2017-10-25T22:08:26+01:00
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignment 2.3.py
# @Last modified by:   Antero Maripuu
# @Last modified time: 2017-11-07T19:38:22+00:00


#Write a program to prompt the user for hours and
#rate per hour to compute gross pay.

inp=float(input("Please enter your hours ")) #Phyton 3 function input(), Python 2.7 raw_input()
inp2=float(input("Please enter your rate (e.g £20.15) "))

def fname(x,y):
  print(x*y)

print("Your calculated cross pay is "),fname(inp, inp2)
