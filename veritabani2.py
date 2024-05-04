
import sqlite3

db= sqlite3.connect("sakila_master.db")
isci=db.cursor()

cumle="""select title,length,rating
        from film 
        where description like '%Boring%'
        and length>=100
        and rating in ('G','PG')
        order by length desc
        limit 5""" #ilk 5i getir ///order by length desc ->> uzundan kisaya siralara /// asc kısadan uzuna-kucukten buyuge

isci.execute(cumle)

satirlar=isci.fetchall()
print("Kayit:",len(satirlar))
for satir in satirlar:
    print(satir[0],satir[1],satir[2])