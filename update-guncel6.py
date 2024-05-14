import sqlite3

db=sqlite3.connect("guncel.db")
isci=db.cursor()

cumle="UPDATE sarkilar  SET playcount=1000 WHERE singer='Duman'"
isci.execute(cumle)
db.commit()