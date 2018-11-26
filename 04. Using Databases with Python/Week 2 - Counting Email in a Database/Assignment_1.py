# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date : 2018-11-25 18:54
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename : Assignment_1.py

"""
create db, create table (org, count) and count number emails per organization

"""

import sqlite3

conn = sqlite3.connect("orgdb.sqlite")
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if fname == "":
    fname = 'mbox-short.txt'

fh = open(fname)

for line in fh:
    if not line.startswith("From: "):
        continue
    pieces = line.split()
    org = pieces[1]
    # print(org)

    cur.execute("SELECT count FROM Counts WHERE org = ? ", (org, ))
    row = cur.fetchone()
    # print(row)
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES ( ?, 1 )''', (org, ))
    else:
        cur.execute('''UPDATE Counts SET count=count+1 WHERE org = ?''', (org, ))

    conn.commit()

sqlstr = "SELECT org, count FROM  Counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(row[0], row[1])

cur.close()