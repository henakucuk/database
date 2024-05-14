import sqlite3

db=sqlite3.connect("guncel.db")
isci=db.cursor()

cumle="UPDATE sarkilar SET earn=playcount*500"
isci.execute(cumle)
db.commit()