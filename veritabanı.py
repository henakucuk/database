
import sqlite3

db=sqlite3.connect("sakila_master.db")
isci=db.cursor()

cumle="select first_name,last_name from actor where first_name like '%PEN%'" # * yerine almasını istediğimiz yeri yazabiliriz mesela, frist_name yazabiliriz (*=hepsi,all)(select * diyebiliriz)
#içinde hen olanları getir demek '%HEN%' eğer '%HEN' --> sonunda hen olanlar, 'HEN%' --> başında hen olan
isci.execute(cumle)

satirlar=isci.fetchall()

for satir in satirlar:
    print(satir[0],satir[1])

