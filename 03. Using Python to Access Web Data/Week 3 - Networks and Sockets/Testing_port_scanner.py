# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date : 2018-11-24 21:22
# @Email:  antero.maripuu@gmail.com
# @Project:  Personal
# @Filename : Testing_port_scanner.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "data.pr4e.org"


def scan_port(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False


for x in range(1,100):
    if scan_port(x):  # if True
        print("Port", x, "is open")
    else:
        print("Port", x, "is closed")

