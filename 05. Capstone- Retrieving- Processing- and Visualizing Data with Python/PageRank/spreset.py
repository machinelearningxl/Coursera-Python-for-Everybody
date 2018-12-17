# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date : 2018-12-17 00:09
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename : spreset.py.py



import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''UPDATE Pages SET new_rank=1.0, old_rank=0.0''')
conn.commit()

cur.close()

print("All pages set to a rank of 1.0")

