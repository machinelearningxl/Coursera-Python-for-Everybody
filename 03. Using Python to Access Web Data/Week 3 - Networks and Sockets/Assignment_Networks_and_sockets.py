# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date : 2018-11-24 00:28
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename : Assignment_Networks_and_sockets.py

"""
Making the HTTP request that will get us the desired document
http://www.pythonlearn.com/code/intro-short.txt
"""

import socket
import  sys

host = "data.pr4e.org"
try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error:
    print("Socket creation failed with error")

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:   #     If no data, break
        print("No Data ERROR")
        break
    else:
        print("RECIVED:")
        print(data.decode())
mysock.close()