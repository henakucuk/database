from bs4 import BeautifulSoup
import requests
import sqlite3

url="https://www.imdb.com/chart/top/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
kaynak = requests.get(url=url, headers=headers).text

soup=BeautifulSoup(kaynak,"html.parser")

vt=sqlite3.connect("ornek.db")
isci=vt.cursor()

movies=soup.find_all("li",attrs={"class":"ipc-metadata-list-summary-item"})
for movie in movies:
    name=movie.h3.text
    span3=movie.find_all("span")[2].text
    cumle=f"""INSERT INTO IMDB(moviename,span3) VALUES ("{name}","{span3}")"""
    
    isci.execute(cumle)
    vt.commit()
vt.close()