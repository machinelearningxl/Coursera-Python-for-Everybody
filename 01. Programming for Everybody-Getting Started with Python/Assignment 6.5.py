# @Author: Antero Maripuu <machinelearningxl>
# @Date:   2017-11-07T14:24:58+00:00
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename: Assignment 6.5.py
# @Last modified by:   machinelearningxl
# @Last modified time: 2017-11-07T14:25:20+00:00

"""
6.5 Write code using find() and string slicing (see section 6.10) to extract
the number at the end of the line below. Convert the extracted value to a
floating point number and print it out. text = "X-DSPAM-Confidence:    0.8475"

Desired Output: 0.8475
"""

text = "X-DSPAM-Confidence:    0.8475"

position = text.find('0')
print(float(text[position + 1:]))