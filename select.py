import sqlalchemy
import psycopg2
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:N7oefgwv@localhost:5432/tasknet')
pprint(engine)

connection = engine.connect()
print(connection)
pprint(engine.table_names())
print()

#1.Название и год выхода альбомов, вышедших в 2018 году
select_1 = connection.execute('''SELECT  name_album, release_data FROM album
WHERE release_data BETWEEN '2018-01-01' AND '2018-12-31';
''').fetchall()
pprint(select_1)
print()

#2.Название и продолжительность самого длительного трека
select_2 = connection.execute('''SELECT   name_track, song_length FROM track
ORDER BY song_length DESC;
''').fetchone()
pprint(select_2)
print()

#3.Название треков, продолжительность которых не менее 3,5 минуты
select_3 = connection.execute('''SELECT  name_track FROM track
WHERE song_length >= 03.50;
''').fetchall()
pprint(select_3)
print()

#4.Названия сборников, вышедших в период с 2018 по 2020 год включительно
select_4 = connection.execute('''SELECT name_collectiom FROM collection
WHERE release_data BETWEEN '2018-01-01' AND '2020-12-31';
''').fetchall()
pprint(select_4)
print()

#5.Исполнители, чье имя состоит из 1 слова
select_5 = connection.execute('''SELECT name_artist FROM artist
WHERE name_artist NOT LIKE '%% %%';
''').fetchall()
pprint(select_5)
print()

#6.Название треков, которые содержат слово "мой"/"my"
select_6 = connection.execute('''SELECT name_track FROM track
WHERE name_track LIKE '%%my%%';
''').fetchall()
pprint(select_6)
