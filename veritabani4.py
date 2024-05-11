
import sqlite3

vt= sqlite3.connect("sakila_master.db")
isci = vt.cursor()

cumle="""select
film.title,actor.first_name,actor.last_name
from film_actor

left join film on film.film_id=film_actor.film_id
left join actor on actor.actor_id=film_actor.actor_id
where film_actor.film_id=10"""

isci.execute(cumle)

satirlar=isci.fetchall()

for satir in satirlar:
    print(satir[0],satir[1],satir[2])