import sqlite3

db=sqlite3.connect("sakila_master.db")
isci=db.cursor()

cumle="SELECT rating,rental_duration,count(*) FROM film WHERE length>120 group by rating,rental_duration"

isci.execute(cumle)
db.commit()