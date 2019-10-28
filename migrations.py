import psycopg2
from config.config import conn_config
from sql_queries.create_query import createTables
from sql_queries.drop_query import dropTables
from sql_queries.insert_query import *
from etl import inject_data
from sql_queries.retrieve_query import retrieve_song

params = conn_config()
conn = psycopg2.connect(**params)
cur = conn.cursor()
            
# DROP TABLES
def drop():
    try:
        for dropTable in dropTables():
            cur.execute(dropTable)
            conn.commit()
        print('Tables Dropped Successfully')
    except psycopg2.Error as e:
        print('Error: Issue dropping tables')
        print(e)
    
    
# CREATE TABLES 
def create():
    try:
        for createTable in createTables():
            cur.execute(createTable)
            conn.commit()
        print('Tables Created Successfully')
    except psycopg2.Error as e:
        print('Error: Issue creating tables')
        print(e)
    

# INSERT TABLES RECORDS
def insert():
#   SONGS
    try:
        for songInserts in inject_data('songs'):
            cur.execute(songs, songInserts)
            conn.commit()
        print('Values for songs Inserted Successfully')
    except psycopg2.Error as e:
        print('Error: Issue inserting values into tables')
        print(e)
#   ARTISTS
    try:
        for artistInserts in inject_data('artists'):
            cur.execute(artists, artistInserts)
            conn.commit()
        print('Values for artist Inserted Successfully')
    except psycopg2.Error as e:
        print('Error: Issue inserting values into tables')
        print(e)
#   USERS
    try:
        for userInserts in inject_data('users'):
            cur.execute(users, userInserts)
            conn.commit()
        print('Values for users Inserted Successfully')
    except psycopg2.Error as e:
        print('Error: Issue inserting values into tables')
        print(e)
        
#   TIME
    try:
        for timeInserts in inject_data('time'):
            cur.execute(time, timeInserts)
            conn.commit()
        print('Values for time Inserted Successfully')
    except psycopg2.Error as e:
        print('Error: Issue inserting values into tables')
        print(e)



#  RETRIEVE VALUES FROM TABLES
def retrieve():
    try:
        cur.execute(retrieve_song)
        results = cur.fetchall()
        return results
    except psycopg2.Error as e:
        print('Error: Issue retrieving values from tables')
        print(e)


