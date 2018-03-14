# @Author: Antero Maripuu <machinelearningxl>
# @Date:   2017-11-07T13:52:47+00:00
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignment 3.3.py
# @Last modified by:   Antero Maripuu
# @Last modified time: 2017-11-08T14:13:13+00:00

#3.3 Write a program to prompt the user for a score using raw_input. Print out
#a letter grade based on the following table:

# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
#If the user enters a value out of range, print a suitable error message and
#exit. For the test, enter a score of 0.85.

try:
    inp=float(input("Please enter a score: "))
except:
    print("Please enter a double number eg. 0.9")
    quit()
def rate(x):
 if x>=0.9 and x<=1.0:
  return "A"
 elif x>=0.8 and x<=0.89:
  return "B"
 elif x>=0.7 and x<=0.79:
  return "C"
 elif x>=0.6 and x<=0.69:
  return "D"
 elif x>=0.0 and x<=0.59:
  return "F"
 else:
  return "Please enter a score between 0.0 and 1.0"

print(rate(inp))
