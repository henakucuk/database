import sqlite3

db=sqlite3.connect("guncel.db")
isci=db.cursor()

#sıfırlama
cumle="UPDATE sarkilar SET playcount=0"
isci.execute(cumle)
db.commit()