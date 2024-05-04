import sqlite3

db= sqlite3.connect("sakila_master.db")
isci=db.cursor()


konu="Action"
adet=10
uzunluk=50
cumle=f"""select title,length,rating
        from film 
        where description like '%{konu}%'
        and length>={uzunluk}
        and rating in ('G','PG')
        order by length desc
        limit {adet}
        """

isci.execute(cumle)

satirlar=isci.fetchall()
print("Kayit:",len(satirlar))
for satir in satirlar:
    print(satir[0],satir[1],satir[2])