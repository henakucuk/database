import sqlite3

db=sqlite3.connect("sakila_master.db")
isci=db.cursor()

cumle="DELETE FROM film WHERE rating='PG'"

isci.execute(cumle)
db.commit()