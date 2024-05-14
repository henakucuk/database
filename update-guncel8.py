import sqlite3

db=sqlite3.connect("guncel.db")
isci=db.cursor()

cumle="DELETE FROM sarkilar WHERE playcount=0"
isci.execute(cumle)
db.commit()