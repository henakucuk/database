import sqlite3

vt=sqlite3.connect("ornek.db")

isci = vt.cursor()

ad=input("Ad giriniz= ")
mat=float(input("Not giriniz= "))

cumle=f"""INSERT INTO ogrenciler(isim,puan) VALUES ('{ad}',{mat})"""

isci.execute(cumle)

vt.commit()
vt.close()